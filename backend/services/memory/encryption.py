"""
Encryption Helper

AES-256 加密助手，用于 SENSITIVE 级别数据加密。

对照 tasks.md 5.4:
- Requirements: 4.2.2
- ⚠️ 陷阱: 不要硬编码密钥，不要日志记录明文

安全设计:
- 密钥从环境变量读取
- 使用 AES-GCM 模式 (认证加密)
- 随机 IV/nonce
- 不记录明文日志
"""

import base64
import logging
import os
import secrets
from typing import Optional

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

logger = logging.getLogger(__name__)


class EncryptionError(Exception):
    """加密错误"""
    pass


class DecryptionError(Exception):
    """解密错误"""
    pass


class EncryptionHelper:
    """
    AES-256-GCM 加密助手
    
    使用 AES-GCM 认证加密模式:
    - 256 位密钥
    - 96 位随机 nonce
    - 128 位认证标签
    
    ⚠️ 重要: 
    - 密钥必须从环境变量获取
    - 绝不记录明文数据
    """
    
    NONCE_SIZE = 12  # 96 bits
    KEY_SIZE = 32    # 256 bits
    
    def __init__(self, key: Optional[bytes] = None):
        """
        初始化加密助手
        
        Args:
            key: 256 位密钥，为 None 时从环境变量 MEMORY_ENCRYPTION_KEY 获取
            
        Raises:
            EncryptionError: 密钥未设置或无效
        """
        if key is None:
            key_b64 = os.getenv("MEMORY_ENCRYPTION_KEY")
            if not key_b64:
                raise EncryptionError(
                    "MEMORY_ENCRYPTION_KEY environment variable not set. "
                    "Generate with: python -c \"import secrets; import base64; "
                    "print(base64.b64encode(secrets.token_bytes(32)).decode())\""
                )
            try:
                key = base64.b64decode(key_b64)
            except Exception:
                raise EncryptionError("Invalid MEMORY_ENCRYPTION_KEY format")
        
        if len(key) != self.KEY_SIZE:
            raise EncryptionError(
                f"Key must be {self.KEY_SIZE} bytes (256 bits), got {len(key)}"
            )
        
        self._aesgcm = AESGCM(key)
        # ⚠️ 不存储密钥明文引用，只存储 AESGCM 对象
    
    def encrypt(self, plaintext: str) -> str:
        """
        加密文本
        
        Args:
            plaintext: 明文
            
        Returns:
            Base64 编码的密文 (nonce + ciphertext)
            
        Raises:
            EncryptionError: 加密失败
        """
        if not plaintext:
            return ""
        
        try:
            # 随机 nonce
            nonce = secrets.token_bytes(self.NONCE_SIZE)
            
            # 加密
            plaintext_bytes = plaintext.encode("utf-8")
            ciphertext = self._aesgcm.encrypt(nonce, plaintext_bytes, None)
            
            # nonce + ciphertext -> base64
            combined = nonce + ciphertext
            result = base64.b64encode(combined).decode("ascii")
            
            # ⚠️ 不记录明文，只记录操作成功
            logger.debug("Encrypted data of %d bytes", len(plaintext_bytes))
            
            return result
        
        except Exception as e:
            # ⚠️ 不记录明文或密文
            logger.error("Encryption failed: %s", type(e).__name__)
            raise EncryptionError(f"Encryption failed: {type(e).__name__}")
    
    def decrypt(self, ciphertext: str) -> str:
        """
        解密文本
        
        Args:
            ciphertext: Base64 编码的密文
            
        Returns:
            明文
            
        Raises:
            DecryptionError: 解密失败
        """
        if not ciphertext:
            return ""
        
        try:
            # base64 -> bytes
            combined = base64.b64decode(ciphertext)
            
            if len(combined) < self.NONCE_SIZE:
                raise DecryptionError("Ciphertext too short")
            
            # 分离 nonce 和 ciphertext
            nonce = combined[:self.NONCE_SIZE]
            encrypted_data = combined[self.NONCE_SIZE:]
            
            # 解密
            plaintext_bytes = self._aesgcm.decrypt(nonce, encrypted_data, None)
            result = plaintext_bytes.decode("utf-8")
            
            # ⚠️ 不记录明文
            logger.debug("Decrypted data of %d bytes", len(plaintext_bytes))
            
            return result
        
        except Exception as e:
            # ⚠️ 不记录密文
            logger.error("Decryption failed: %s", type(e).__name__)
            raise DecryptionError(f"Decryption failed: {type(e).__name__}")
    
    @staticmethod
    def generate_key() -> str:
        """
        生成新的 256 位密钥
        
        Returns:
            Base64 编码的密钥
        """
        key = secrets.token_bytes(EncryptionHelper.KEY_SIZE)
        return base64.b64encode(key).decode("ascii")
