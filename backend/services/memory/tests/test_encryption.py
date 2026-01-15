"""
Encryption Helper Tests

对照 tasks.md 5.4, 5.6:
- Requirements: 4.2.2, 8.1.1
"""

import pytest
import base64
import secrets
from hypothesis import given, strategies as st, settings

from backend.services.memory.encryption import (
    EncryptionHelper,
    EncryptionError,
    DecryptionError,
)


class TestEncryptionBasic:
    """加密基础测试"""
    
    def test_encrypt_decrypt_round_trip(self, encryption_helper):
        """测试加密解密往返"""
        plaintext = "Hello, World! 你好世界！"
        
        ciphertext = encryption_helper.encrypt(plaintext)
        decrypted = encryption_helper.decrypt(ciphertext)
        
        assert decrypted == plaintext
    
    def test_empty_string(self, encryption_helper):
        """测试空字符串"""
        assert encryption_helper.encrypt("") == ""
        assert encryption_helper.decrypt("") == ""
    
    def test_unicode_text(self, encryption_helper):
        """测试 Unicode 文本"""
        plaintext = "🎉 测试文本 émojis 日本語 한국어"
        
        ciphertext = encryption_helper.encrypt(plaintext)
        decrypted = encryption_helper.decrypt(ciphertext)
        
        assert decrypted == plaintext
    
    def test_long_text(self, encryption_helper):
        """测试长文本"""
        plaintext = "x" * 10000
        
        ciphertext = encryption_helper.encrypt(plaintext)
        decrypted = encryption_helper.decrypt(ciphertext)
        
        assert decrypted == plaintext
    
    def test_same_plaintext_different_ciphertext(self, encryption_helper):
        """测试相同明文产生不同密文 (随机 nonce)"""
        plaintext = "Same text"
        
        ciphertext1 = encryption_helper.encrypt(plaintext)
        ciphertext2 = encryption_helper.encrypt(plaintext)
        
        # 由于随机 nonce，密文应该不同
        assert ciphertext1 != ciphertext2
        
        # 但都能解密回原文
        assert encryption_helper.decrypt(ciphertext1) == plaintext
        assert encryption_helper.decrypt(ciphertext2) == plaintext


class TestEncryptionErrors:
    """加密错误测试"""
    
    def test_invalid_key_length(self):
        """测试无效密钥长度"""
        with pytest.raises(EncryptionError):
            EncryptionHelper(key=b"short")
    
    def test_decrypt_invalid_ciphertext(self, encryption_helper):
        """测试解密无效密文"""
        with pytest.raises(DecryptionError):
            encryption_helper.decrypt("invalid_base64_!@#$")
    
    def test_decrypt_tampered_ciphertext(self, encryption_helper):
        """测试解密被篡改的密文"""
        plaintext = "Secret data"
        ciphertext = encryption_helper.encrypt(plaintext)
        
        # 篡改密文
        tampered = ciphertext[:-4] + "XXXX"
        
        with pytest.raises(DecryptionError):
            encryption_helper.decrypt(tampered)
    
    def test_decrypt_too_short(self, encryption_helper):
        """测试解密过短密文"""
        with pytest.raises(DecryptionError):
            encryption_helper.decrypt(base64.b64encode(b"short").decode())


class TestEncryptionKeyGeneration:
    """密钥生成测试"""
    
    def test_generate_key(self):
        """测试生成密钥"""
        key_b64 = EncryptionHelper.generate_key()
        
        # 应该是有效的 base64
        key_bytes = base64.b64decode(key_b64)
        
        # 应该是 32 字节
        assert len(key_bytes) == 32
    
    def test_generated_key_is_random(self):
        """测试生成的密钥是随机的"""
        key1 = EncryptionHelper.generate_key()
        key2 = EncryptionHelper.generate_key()
        
        assert key1 != key2
    
    def test_generated_key_is_usable(self):
        """测试生成的密钥可用"""
        key_b64 = EncryptionHelper.generate_key()
        key_bytes = base64.b64decode(key_b64)
        
        helper = EncryptionHelper(key=key_bytes)
        
        plaintext = "Test"
        ciphertext = helper.encrypt(plaintext)
        decrypted = helper.decrypt(ciphertext)
        
        assert decrypted == plaintext


class TestEncryptionProperty:
    """加密属性测试"""
    
    @given(plaintext=st.text(min_size=0, max_size=1000))
    @settings(max_examples=50)
    def test_encrypt_decrypt_property(self, plaintext):
        """属性测试: 加密解密往返一致性"""
        # 创建本地实例避免 fixture 问题
        key = secrets.token_bytes(32)
        helper = EncryptionHelper(key=key)
        
        ciphertext = helper.encrypt(plaintext)
        decrypted = helper.decrypt(ciphertext)
        
        assert decrypted == plaintext
    
    @given(plaintext=st.text(min_size=1, max_size=100))
    @settings(max_examples=20)
    def test_ciphertext_format(self, plaintext):
        """属性测试: 密文格式是有效 base64"""
        key = secrets.token_bytes(32)
        helper = EncryptionHelper(key=key)
        
        ciphertext = helper.encrypt(plaintext)
        
        # 应该是有效的 base64
        decoded = base64.b64decode(ciphertext)
        
        # 应该至少包含 nonce (12 bytes) + 数据
        assert len(decoded) >= 12
