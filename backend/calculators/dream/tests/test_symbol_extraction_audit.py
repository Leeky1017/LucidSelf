# backend/calculators/dream/tests/test_symbol_extraction_audit.py
"""
Symbol Extraction Accuracy Audit Tests

审计符号提取准确性 - 验证人物、动物、场景、行为识别
Requirements: 7.1

This module audits the DreamExtractor's ability to correctly identify and
categorize dream symbols across all supported categories:
- animal: 动物符号
- person: 人物符号  
- scene: 场景符号
- object: 物品符号
- nature: 自然符号
- body: 身体符号
"""

import pytest
from typing import List, Tuple, Dict, Set

from backend.calculators.dream import (
    DreamExtractor,
    DreamInput,
    DreamFactors,
    DreamSymbol,
    SYMBOL_CATEGORIES,
    THEMES,
    EMOTIONS,
)


class TestAnimalSymbolExtraction:
    """Audit tests for animal symbol extraction accuracy."""
    
    @pytest.fixture
    def extractor(self):
        return DreamExtractor()
    
    # Chinese animal symbol test cases
    ZH_ANIMAL_CASES = [
        ("我梦见一只狗在追我，感觉很害怕", ["dog"]),
        ("梦里有一条蛇在草丛中爬行，很可怕", ["snake"]),
        ("我看到一只蝴蝶飞过花园，很美丽", ["butterfly"]),
        ("梦中有一只猫在窗台上睡觉，很安静", ["cat"]),
        ("我梦见一条鱼在水里游泳，很自由", ["fish"]),
        ("梦里有一匹马在草原上奔跑，很壮观", ["horse"]),
        ("我看到一条龙在天空中飞翔，很震撼", ["dragon"]),
        ("梦中有一只老虎在森林里行走，很威严", ["tiger"]),
        ("我梦见一只狼在月光下嚎叫，很孤独", ["wolf"]),
        ("梦里有一只蜘蛛在织网，很专注", ["spider"]),
        ("我看到一只鸟在树上唱歌，很悦耳", ["bird"]),
        ("梦中有一只老鼠在角落里躲藏，很害怕", ["rat"]),
    ]
    
    # English animal symbol test cases
    EN_ANIMAL_CASES = [
        ("I dreamed of a dog chasing me through the park", ["dog"]),
        ("There was a snake slithering in the grass in my dream", ["snake"]),
        ("I saw a beautiful butterfly flying in the garden", ["butterfly"]),
        ("A cat was sleeping on the windowsill in my dream", ["cat"]),
        ("I dreamed of fish swimming in clear water", ["fish"]),
        ("There was a horse running across the meadow", ["horse"]),
        ("I saw a dragon flying in the sky in my dream", ["dragon"]),
        ("A tiger was walking through the forest", ["tiger"]),
        ("I dreamed of a wolf howling at the moon", ["wolf"]),
        ("There was a spider weaving its web in my dream", ["spider"]),
        ("I saw a bird singing in the tree in my dream", ["bird"]),
        ("A rat was hiding in the corner in my dream", ["rat"]),
    ]
    
    @pytest.mark.parametrize("dream_text,expected_symbols", ZH_ANIMAL_CASES)
    def test_chinese_animal_extraction(self, extractor, dream_text: str, expected_symbols: List[str]):
        """Test Chinese animal symbol extraction accuracy."""
        input_data = DreamInput(dream_text=dream_text, language="zh")
        result = extractor.extract(input_data)
        
        extracted_animals = [s.symbol for s in result.symbols if s.category == "animal"]
        
        for expected in expected_symbols:
            assert expected in extracted_animals, \
                f"Expected animal '{expected}' not found in '{dream_text}'. Found: {extracted_animals}"
    
    @pytest.mark.parametrize("dream_text,expected_symbols", EN_ANIMAL_CASES)
    def test_english_animal_extraction(self, extractor, dream_text: str, expected_symbols: List[str]):
        """Test English animal symbol extraction accuracy."""
        input_data = DreamInput(dream_text=dream_text, language="en")
        result = extractor.extract(input_data)
        
        extracted_animals = [s.symbol for s in result.symbols if s.category == "animal"]
        
        for expected in expected_symbols:
            assert expected in extracted_animals, \
                f"Expected animal '{expected}' not found in '{dream_text}'. Found: {extracted_animals}"


class TestPersonSymbolExtraction:
    """Audit tests for person symbol extraction accuracy."""
    
    @pytest.fixture
    def extractor(self):
        return DreamExtractor()
    
    # Chinese person symbol test cases
    ZH_PERSON_CASES = [
        ("我梦见我的母亲在厨房做饭，很温馨", ["mother"]),
        ("梦里我的父亲在教我骑自行车，很开心", ["father"]),
        ("我看到一个孩子在公园里玩耍，很天真", ["child"]),
        ("梦中有一个陌生人向我走来，很紧张", ["stranger"]),
        ("我梦见我的朋友在和我聊天，很愉快", ["friend"]),
        ("梦里我的恋人在等我，很甜蜜", ["lover"]),
        ("我看到我的老师在讲课，很认真", ["teacher"]),
        ("梦中我的老板在开会，很严肃", ["boss"]),
        ("我梦见一个婴儿在哭泣，很心疼", ["baby"]),
        ("梦里有一个老人在散步，很安详", ["elderly"]),
    ]
    
    # English person symbol test cases
    EN_PERSON_CASES = [
        ("I dreamed of my mother cooking in the kitchen", ["mother"]),
        ("My father was teaching me to ride a bike in my dream", ["father"]),
        ("I saw a child playing in the park in my dream", ["child"]),
        ("A stranger was walking towards me in my dream", ["stranger"]),
        ("I dreamed of my friend talking to me happily", ["friend"]),
        ("My lover was waiting for me in my dream", ["lover"]),
        ("I saw my teacher giving a lecture in my dream", ["teacher"]),
        ("My boss was having a meeting in my dream", ["boss"]),
        ("I dreamed of a baby crying in the room", ["baby"]),
        ("An elderly person was walking slowly in my dream", ["elderly"]),
    ]
    
    @pytest.mark.parametrize("dream_text,expected_symbols", ZH_PERSON_CASES)
    def test_chinese_person_extraction(self, extractor, dream_text: str, expected_symbols: List[str]):
        """Test Chinese person symbol extraction accuracy."""
        input_data = DreamInput(dream_text=dream_text, language="zh")
        result = extractor.extract(input_data)
        
        extracted_persons = [s.symbol for s in result.symbols if s.category == "person"]
        
        for expected in expected_symbols:
            assert expected in extracted_persons, \
                f"Expected person '{expected}' not found in '{dream_text}'. Found: {extracted_persons}"
    
    @pytest.mark.parametrize("dream_text,expected_symbols", EN_PERSON_CASES)
    def test_english_person_extraction(self, extractor, dream_text: str, expected_symbols: List[str]):
        """Test English person symbol extraction accuracy."""
        input_data = DreamInput(dream_text=dream_text, language="en")
        result = extractor.extract(input_data)
        
        extracted_persons = [s.symbol for s in result.symbols if s.category == "person"]
        
        for expected in expected_symbols:
            assert expected in extracted_persons, \
                f"Expected person '{expected}' not found in '{dream_text}'. Found: {extracted_persons}"


class TestSceneSymbolExtraction:
    """Audit tests for scene symbol extraction accuracy."""
    
    @pytest.fixture
    def extractor(self):
        return DreamExtractor()
    
    # Chinese scene symbol test cases
    ZH_SCENE_CASES = [
        ("我梦见自己在一个房子里迷路了，很焦虑", ["house"]),
        ("梦里我回到了学校，在教室里上课", ["school"]),
        ("我看到自己在森林里行走，很神秘", ["forest"]),
        ("梦中我在一条路上奔跑，不知道去哪", ["road"]),
        ("我梦见自己站在一座桥上，看着河水", ["bridge"]),
        ("梦里我在爬一座山，很累但很坚持", ["mountain"]),
        ("我看到自己在一个洞里探险，很刺激", ["cave"]),
        ("梦中我在医院里等待，很担心", ["hospital"]),
        ("我梦见自己在寺庙里祈祷，很虔诚", ["temple"]),
        ("梦里我在墓地里行走，很阴森", ["cemetery"]),
    ]
    
    # English scene symbol test cases
    EN_SCENE_CASES = [
        ("I dreamed of being lost in a house, feeling anxious", ["house"]),
        ("I was back at school in my dream, sitting in a classroom", ["school"]),
        ("I saw myself walking through a forest in my dream", ["forest"]),
        ("I was running on a road in my dream, not knowing where to go", ["road"]),
        ("I dreamed of standing on a bridge, watching the water", ["bridge"]),
        ("I was climbing a mountain in my dream, tired but determined", ["mountain"]),
        ("I saw myself exploring a cave in my dream, very exciting", ["cave"]),
        ("I was waiting in a hospital in my dream, feeling worried", ["hospital"]),
        ("I dreamed of praying in a temple, feeling devout", ["temple"]),
        ("I was walking through a cemetery in my dream, very eerie", ["cemetery"]),
    ]
    
    @pytest.mark.parametrize("dream_text,expected_symbols", ZH_SCENE_CASES)
    def test_chinese_scene_extraction(self, extractor, dream_text: str, expected_symbols: List[str]):
        """Test Chinese scene symbol extraction accuracy."""
        input_data = DreamInput(dream_text=dream_text, language="zh")
        result = extractor.extract(input_data)
        
        extracted_scenes = [s.symbol for s in result.symbols if s.category == "scene"]
        
        for expected in expected_symbols:
            assert expected in extracted_scenes, \
                f"Expected scene '{expected}' not found in '{dream_text}'. Found: {extracted_scenes}"
    
    @pytest.mark.parametrize("dream_text,expected_symbols", EN_SCENE_CASES)
    def test_english_scene_extraction(self, extractor, dream_text: str, expected_symbols: List[str]):
        """Test English scene symbol extraction accuracy."""
        input_data = DreamInput(dream_text=dream_text, language="en")
        result = extractor.extract(input_data)
        
        extracted_scenes = [s.symbol for s in result.symbols if s.category == "scene"]
        
        for expected in expected_symbols:
            assert expected in extracted_scenes, \
                f"Expected scene '{expected}' not found in '{dream_text}'. Found: {extracted_scenes}"


class TestNatureSymbolExtraction:
    """Audit tests for nature symbol extraction accuracy."""
    
    @pytest.fixture
    def extractor(self):
        return DreamExtractor()
    
    # Chinese nature symbol test cases
    ZH_NATURE_CASES = [
        ("我梦见自己在水里游泳，感觉很自由", ["water"]),
        ("梦里我看到了大海，波涛汹涌", ["sea"]),
        ("我看到一条河在流淌，很平静", ["river"]),
        ("梦中有一场大火，很危险", ["fire"]),
        ("我梦见下雨了，淋湿了全身", ["rain"]),
        ("梦里下雪了，到处都是白色", ["snow"]),
        ("我看到太阳升起，很温暖", ["sun"]),
        ("梦中月亮很亮，照亮了夜空", ["moon"]),
        ("我梦见满天星星，很美丽", ["star"]),
        ("梦里天空很蓝，万里无云", ["sky"]),
        ("我看到云彩飘过，变幻莫测", ["cloud"]),
        ("梦中刮起了大风，很冷", ["wind"]),
        ("我梦见一棵大树，枝繁叶茂", ["tree"]),
        ("梦里有很多花，五颜六色", ["flower"]),
    ]
    
    # English nature symbol test cases
    EN_NATURE_CASES = [
        ("I dreamed of swimming in the water, feeling free", ["water"]),
        ("I saw the sea in my dream, with huge waves", ["sea"]),
        ("I saw a river flowing peacefully in my dream", ["river"]),
        ("There was a big fire in my dream, very dangerous", ["fire"]),
        ("I dreamed of rain falling, getting completely wet", ["rain"]),
        ("It was snowing in my dream, everything was white", ["snow"]),
        ("I saw the sun rising in my dream, very warm", ["sun"]),
        ("The moon was bright in my dream, lighting up the night", ["moon"]),
        ("I dreamed of stars filling the sky, very beautiful", ["star"]),
        ("The sky was blue in my dream, without any clouds", ["sky"]),
        ("I saw clouds floating by in my dream, ever-changing", ["cloud"]),
        ("There was strong wind in my dream, very cold", ["wind"]),
        ("I dreamed of a big tree with lush branches", ["tree"]),
        ("There were many flowers in my dream, colorful", ["flower"]),
    ]
    
    @pytest.mark.parametrize("dream_text,expected_symbols", ZH_NATURE_CASES)
    def test_chinese_nature_extraction(self, extractor, dream_text: str, expected_symbols: List[str]):
        """Test Chinese nature symbol extraction accuracy."""
        input_data = DreamInput(dream_text=dream_text, language="zh")
        result = extractor.extract(input_data)
        
        extracted_nature = [s.symbol for s in result.symbols if s.category == "nature"]
        
        for expected in expected_symbols:
            assert expected in extracted_nature, \
                f"Expected nature '{expected}' not found in '{dream_text}'. Found: {extracted_nature}"
    
    @pytest.mark.parametrize("dream_text,expected_symbols", EN_NATURE_CASES)
    def test_english_nature_extraction(self, extractor, dream_text: str, expected_symbols: List[str]):
        """Test English nature symbol extraction accuracy."""
        input_data = DreamInput(dream_text=dream_text, language="en")
        result = extractor.extract(input_data)
        
        extracted_nature = [s.symbol for s in result.symbols if s.category == "nature"]
        
        for expected in expected_symbols:
            assert expected in extracted_nature, \
                f"Expected nature '{expected}' not found in '{dream_text}'. Found: {extracted_nature}"


class TestObjectSymbolExtraction:
    """Audit tests for object symbol extraction accuracy."""
    
    @pytest.fixture
    def extractor(self):
        return DreamExtractor()
    
    # Chinese object symbol test cases
    ZH_OBJECT_CASES = [
        ("我梦见找到了一把钥匙，打开了一扇门", ["key", "door"]),
        ("梦里我看着镜子，看到了自己的倒影", ["mirror"]),
        ("我在梦中读一本书，内容很有趣", ["book"]),
        ("梦里我捡到了很多钱，感觉很开心", ["money"]),
        ("我梦见手机响了，但找不到在哪", ["phone"]),
        ("梦中我在开车，在路上行驶", ["car"]),
        ("我看到一扇窗户，外面是美丽的风景", ["window"]),
        ("梦里有一把刀，很锋利", ["knife"]),
        ("我梦见一枚戒指，闪闪发光", ["ring"]),
        ("梦中我在整理衣服，准备出门", ["clothes"]),
    ]
    
    # English object symbol test cases
    EN_OBJECT_CASES = [
        ("I dreamed of finding a key and opening a door", ["key", "door"]),
        ("I was looking at a mirror in my dream, seeing my reflection", ["mirror"]),
        ("I was reading a book in my dream, very interesting", ["book"]),
        ("I found a lot of money in my dream, feeling happy", ["money"]),
        ("I dreamed my phone was ringing but I could not find it", ["phone"]),
        ("I was driving a car in my dream, on the road", ["car"]),
        ("I saw a window with beautiful scenery outside", ["window"]),
        ("There was a knife in my dream, very sharp", ["knife"]),
        ("I dreamed of a ring, shining brightly", ["ring"]),
        ("I was organizing my clothes in my dream, getting ready", ["clothes"]),
    ]
    
    @pytest.mark.parametrize("dream_text,expected_symbols", ZH_OBJECT_CASES)
    def test_chinese_object_extraction(self, extractor, dream_text: str, expected_symbols: List[str]):
        """Test Chinese object symbol extraction accuracy."""
        input_data = DreamInput(dream_text=dream_text, language="zh")
        result = extractor.extract(input_data)
        
        extracted_objects = [s.symbol for s in result.symbols if s.category == "object"]
        
        for expected in expected_symbols:
            assert expected in extracted_objects, \
                f"Expected object '{expected}' not found in '{dream_text}'. Found: {extracted_objects}"
    
    @pytest.mark.parametrize("dream_text,expected_symbols", EN_OBJECT_CASES)
    def test_english_object_extraction(self, extractor, dream_text: str, expected_symbols: List[str]):
        """Test English object symbol extraction accuracy."""
        input_data = DreamInput(dream_text=dream_text, language="en")
        result = extractor.extract(input_data)
        
        extracted_objects = [s.symbol for s in result.symbols if s.category == "object"]
        
        for expected in expected_symbols:
            assert expected in extracted_objects, \
                f"Expected object '{expected}' not found in '{dream_text}'. Found: {extracted_objects}"


class TestBodySymbolExtraction:
    """Audit tests for body symbol extraction accuracy."""
    
    @pytest.fixture
    def extractor(self):
        return DreamExtractor()
    
    # Chinese body symbol test cases
    ZH_BODY_CASES = [
        ("我梦见牙齿掉了，感觉很恐慌", ["teeth"]),
        ("梦里我的头发变白了，很惊讶", ["hair"]),
        ("我看到自己的手在发抖，很紧张", ["hand"]),
        ("梦中我的眼睛看不见了，很害怕", ["eye"]),
        ("我梦见流了很多血，很担心", ["blood"]),
        ("梦里我的心跳得很快，很紧张", ["heart"]),
        ("我看到自己的脚受伤了，很疼", ["foot"]),
        ("梦中我的脸变了样，认不出自己", ["face"]),
        ("我梦见头很疼，像要裂开一样", ["head"]),
    ]
    
    # English body symbol test cases
    EN_BODY_CASES = [
        ("I dreamed my teeth were falling out, feeling panicked", ["teeth"]),
        ("My hair turned white in my dream, very surprised", ["hair"]),
        ("I saw my hands shaking in my dream, feeling nervous", ["hand"]),
        ("I could not see with my eyes in my dream, very scared", ["eye"]),
        ("I dreamed of bleeding a lot, feeling worried", ["blood"]),
        ("My heart was beating fast in my dream, very nervous", ["heart"]),
        ("I saw my foot was injured in my dream, very painful", ["foot"]),
        ("My face changed in my dream, could not recognize myself", ["face"]),
        ("I dreamed my head was hurting badly, like splitting", ["head"]),
    ]
    
    @pytest.mark.parametrize("dream_text,expected_symbols", ZH_BODY_CASES)
    def test_chinese_body_extraction(self, extractor, dream_text: str, expected_symbols: List[str]):
        """Test Chinese body symbol extraction accuracy."""
        input_data = DreamInput(dream_text=dream_text, language="zh")
        result = extractor.extract(input_data)
        
        extracted_body = [s.symbol for s in result.symbols if s.category == "body"]
        
        for expected in expected_symbols:
            assert expected in extracted_body, \
                f"Expected body '{expected}' not found in '{dream_text}'. Found: {extracted_body}"
    
    @pytest.mark.parametrize("dream_text,expected_symbols", EN_BODY_CASES)
    def test_english_body_extraction(self, extractor, dream_text: str, expected_symbols: List[str]):
        """Test English body symbol extraction accuracy."""
        input_data = DreamInput(dream_text=dream_text, language="en")
        result = extractor.extract(input_data)
        
        extracted_body = [s.symbol for s in result.symbols if s.category == "body"]
        
        for expected in expected_symbols:
            assert expected in extracted_body, \
                f"Expected body '{expected}' not found in '{dream_text}'. Found: {extracted_body}"


class TestMultiCategoryExtraction:
    """Audit tests for extracting symbols from multiple categories in one dream."""
    
    @pytest.fixture
    def extractor(self):
        return DreamExtractor()
    
    def test_chinese_multi_category_dream(self, extractor):
        """Test extraction of multiple categories from a complex Chinese dream."""
        dream_text = "我梦见我的母亲带着一只狗在森林里散步，天上有月亮，我手里拿着一把钥匙"
        input_data = DreamInput(dream_text=dream_text, language="zh")
        result = extractor.extract(input_data)
        
        # Should find symbols from multiple categories
        categories_found = set(s.category for s in result.symbols)
        
        # Expect: person (母亲), animal (狗), scene (森林), nature (月亮), object (钥匙), body (手)
        assert "person" in categories_found, "Should find person category"
        assert "animal" in categories_found, "Should find animal category"
        assert "scene" in categories_found, "Should find scene category"
        assert "nature" in categories_found, "Should find nature category"
        assert "object" in categories_found, "Should find object category"
    
    def test_english_multi_category_dream(self, extractor):
        """Test extraction of multiple categories from a complex English dream."""
        dream_text = "I dreamed of my mother walking with a dog in the forest, the moon was shining, and I was holding a key in my hand"
        input_data = DreamInput(dream_text=dream_text, language="en")
        result = extractor.extract(input_data)
        
        # Should find symbols from multiple categories
        categories_found = set(s.category for s in result.symbols)
        
        # Expect: person (mother), animal (dog), scene (forest), nature (moon), object (key), body (hand)
        assert "person" in categories_found, "Should find person category"
        assert "animal" in categories_found, "Should find animal category"
        assert "scene" in categories_found, "Should find scene category"
        assert "nature" in categories_found, "Should find nature category"
        assert "object" in categories_found, "Should find object category"


class TestSymbolExtractionCoverage:
    """Audit tests for overall symbol extraction coverage."""
    
    @pytest.fixture
    def extractor(self):
        return DreamExtractor()
    
    def test_all_categories_supported(self, extractor):
        """Verify all defined categories are supported."""
        supported = extractor.get_supported_categories()
        
        for category in SYMBOL_CATEGORIES:
            assert category in supported, f"Category '{category}' should be supported"
    
    def test_category_count(self, extractor):
        """Verify the expected number of categories."""
        supported = extractor.get_supported_categories()
        
        # Should have 6 categories: animal, person, scene, object, nature, body
        assert len(supported) == 6, f"Expected 6 categories, got {len(supported)}"
    
    def test_chinese_symbol_dictionary_coverage(self, extractor):
        """Verify Chinese symbol dictionary has entries for all categories."""
        # Test that each category has at least one symbol that can be extracted
        # Note: DreamInput requires at least 10 characters
        test_texts = {
            "animal": "我梦见一只狗在追我，感觉很害怕",
            "person": "我梦见我的母亲在厨房做饭，很温馨",
            "scene": "我梦见自己在房子里迷路了，很焦虑",
            "object": "我梦见找到一把钥匙，打开了门",
            "nature": "我梦见大海波涛汹涌，很壮观",
            "body": "我梦见牙齿掉了很多，感觉很恐慌",
        }
        
        for category, text in test_texts.items():
            input_data = DreamInput(dream_text=text, language="zh")
            result = extractor.extract(input_data)
            
            category_symbols = [s for s in result.symbols if s.category == category]
            assert len(category_symbols) > 0, \
                f"No symbols found for category '{category}' in text: {text}"
    
    def test_english_symbol_dictionary_coverage(self, extractor):
        """Verify English symbol dictionary has entries for all categories."""
        # Test that each category has at least one symbol that can be extracted
        test_texts = {
            "animal": "I dreamed of a dog chasing me",
            "person": "I dreamed of my mother cooking",
            "scene": "I dreamed of being lost in a house",
            "object": "I dreamed of finding a key",
            "nature": "I dreamed of the sea with huge waves",
            "body": "I dreamed my teeth were falling out",
        }
        
        for category, text in test_texts.items():
            input_data = DreamInput(dream_text=text, language="en")
            result = extractor.extract(input_data)
            
            category_symbols = [s for s in result.symbols if s.category == category]
            assert len(category_symbols) > 0, \
                f"No symbols found for category '{category}' in text: {text}"



# =============================================================================
# Emotion Detection Audit Tests
# =============================================================================

class TestEmotionDetectionAudit:
    """
    Audit tests for emotion detection accuracy.
    
    Validates: Requirements 7.3 - 验证情绪基调判断正确
    """
    
    @pytest.fixture
    def extractor(self):
        return DreamExtractor()
    
    # Chinese emotion test cases
    ZH_EMOTION_CASES = [
        ("我梦见被追赶，感觉非常害怕和恐惧", ["fear"]),
        ("梦里我很高兴，感觉非常快乐和幸福", ["joy"]),
        ("我梦见考试，感觉很焦虑和紧张", ["anxiety"]),
        ("梦中一切都很平静，感觉很安静祥和", ["calm"]),
        ("我梦见和人吵架，感觉很愤怒生气", ["anger"]),
        ("梦里我在哭泣，感觉很悲伤难过", ["sadness"]),
        ("我梦见迷路了，感觉很困惑茫然", ["confusion"]),
        ("梦中我很兴奋，感觉非常激动", ["excitement"]),
        ("我梦见在海边，感觉很安宁舒适", ["peace"]),
        ("梦里发生了意外，感觉很惊讶吃惊", ["surprise"]),
    ]
    
    # English emotion test cases
    EN_EMOTION_CASES = [
        ("I dreamed of being chased, feeling very scared and afraid", ["fear"]),
        ("In my dream I was happy, feeling joyful and delighted", ["joy"]),
        ("I dreamed of an exam, feeling anxious and nervous", ["anxiety"]),
        ("Everything was calm in my dream, feeling peaceful and serene", ["calm"]),
        ("I dreamed of arguing with someone, feeling angry and furious", ["anger"]),
        ("In my dream I was crying, feeling sad and sorrowful", ["sadness"]),
        ("I dreamed of being lost, feeling confused and puzzled", ["confusion"]),
        ("In my dream I was excited, feeling thrilled and exhilarated", ["excitement"]),
        ("I dreamed of being at the beach, feeling peaceful and content", ["peace"]),
        ("Something unexpected happened in my dream, feeling surprised and shocked", ["surprise"]),
    ]
    
    @pytest.mark.parametrize("dream_text,expected_emotions", ZH_EMOTION_CASES)
    def test_chinese_emotion_detection(self, extractor, dream_text: str, expected_emotions: List[str]):
        """Test Chinese emotion detection accuracy."""
        input_data = DreamInput(dream_text=dream_text, language="zh")
        result = extractor.extract(input_data)
        
        for expected in expected_emotions:
            assert expected in result.emotions, \
                f"Expected emotion '{expected}' not found in '{dream_text}'. Found: {result.emotions}"
    
    @pytest.mark.parametrize("dream_text,expected_emotions", EN_EMOTION_CASES)
    def test_english_emotion_detection(self, extractor, dream_text: str, expected_emotions: List[str]):
        """Test English emotion detection accuracy."""
        input_data = DreamInput(dream_text=dream_text, language="en")
        result = extractor.extract(input_data)
        
        for expected in expected_emotions:
            assert expected in result.emotions, \
                f"Expected emotion '{expected}' not found in '{dream_text}'. Found: {result.emotions}"
    
    def test_all_emotions_supported(self, extractor):
        """Verify all defined emotions are supported."""
        supported = extractor.get_supported_emotions()
        
        for emotion in EMOTIONS:
            assert emotion in supported, f"Emotion '{emotion}' should be supported"
    
    def test_emotion_count(self, extractor):
        """Verify the expected number of emotions."""
        supported = extractor.get_supported_emotions()
        
        # Should have 10 emotions
        assert len(supported) == 10, f"Expected 10 emotions, got {len(supported)}"
    
    def test_multiple_emotions_in_one_dream(self, extractor):
        """Test detection of multiple emotions in a single dream."""
        # Chinese dream with multiple emotions
        dream_text = "我梦见被追赶，感觉很害怕，但后来逃脱了，感觉很高兴和兴奋"
        input_data = DreamInput(dream_text=dream_text, language="zh")
        result = extractor.extract(input_data)
        
        # Should detect multiple emotions
        assert len(result.emotions) >= 2, \
            f"Expected multiple emotions, found: {result.emotions}"
    
    def test_emotion_factor_matrix_format(self, extractor):
        """Test that emotion factors follow the correct naming convention."""
        dream_text = "我梦见被追赶，感觉非常害怕和恐惧"
        input_data = DreamInput(dream_text=dream_text, language="zh")
        result = extractor.extract(input_data)
        factor_matrix = result.to_factor_matrix()
        
        # Check that emotion factors have correct prefix
        emotion_factors = [f for f in factor_matrix.factors.keys() if f.startswith("dream_emotion_")]
        
        assert len(emotion_factors) > 0, "Should have at least one emotion factor"
        
        for factor_id in emotion_factors:
            # Factor ID should be dream_emotion_{emotion_name}
            parts = factor_id.split("_")
            assert len(parts) >= 3, f"Invalid emotion factor format: {factor_id}"
            assert parts[0] == "dream", f"Factor should start with 'dream': {factor_id}"
            assert parts[1] == "emotion", f"Factor should have 'emotion' as second part: {factor_id}"


class TestThemeDetectionAudit:
    """
    Audit tests for theme detection accuracy.
    
    Validates: Requirements 7.1 - Theme detection is part of symbol extraction
    """
    
    @pytest.fixture
    def extractor(self):
        return DreamExtractor()
    
    # Chinese theme test cases
    ZH_THEME_CASES = [
        ("我梦见被人追赶，拼命逃跑", ["chase"]),
        ("梦里我从高处坠落，不断往下掉", ["falling"]),
        ("我梦见自己在飞翔，飘浮在空中", ["flying"]),
        ("梦中我在考试，试卷很难", ["exam"]),
        ("我梦见有人死亡，参加了葬礼", ["death"]),
        ("梦里我在水里游泳，差点溺水", ["water"]),
        ("我梦见迷路了，找不到回家的路", ["lost"]),
        ("梦中我没穿衣服，感觉很尴尬", ["naked"]),
        ("我梦见牙齿掉了，一颗接一颗", ["teeth"]),
        ("梦里我迟到了，赶不上火车", ["late"]),
        ("我梦见被困住了，出不去", ["trapped"]),
        ("梦中我和老朋友重逢，很开心", ["reunion"]),
        ("我梦见去旅行，在路上远行", ["journey"]),
        ("梦里我和人打架，发生了冲突", ["conflict"]),
        ("我梦见自己变成了一只鸟", ["transformation"]),
    ]
    
    # English theme test cases
    EN_THEME_CASES = [
        ("I dreamed of being chased, running away desperately", ["chase"]),
        ("In my dream I was falling from a high place, plummeting down", ["falling"]),
        ("I dreamed of flying, soaring through the sky", ["flying"]),
        ("In my dream I was taking an exam, the test was very hard", ["exam"]),
        ("I dreamed of someone dying, attending a funeral", ["death"]),
        ("In my dream I was swimming in water, almost drowning", ["water"]),
        ("I dreamed of being lost, could not find my way home", ["lost"]),
        ("In my dream I was naked, feeling very embarrassed", ["naked"]),
        ("I dreamed my teeth were falling out, one by one", ["teeth"]),
        ("In my dream I was running late, missing the train", ["late"]),
        ("I dreamed of being trapped, could not escape", ["trapped"]),
        ("In my dream I was reunited with old friends, very happy", ["reunion"]),
        ("I dreamed of traveling, on a long journey", ["journey"]),
        ("In my dream I was fighting with someone, a big conflict", ["conflict"]),
        ("I dreamed of transforming into a bird, becoming something else", ["transformation"]),
    ]
    
    @pytest.mark.parametrize("dream_text,expected_themes", ZH_THEME_CASES)
    def test_chinese_theme_detection(self, extractor, dream_text: str, expected_themes: List[str]):
        """Test Chinese theme detection accuracy."""
        input_data = DreamInput(dream_text=dream_text, language="zh")
        result = extractor.extract(input_data)
        
        for expected in expected_themes:
            assert expected in result.themes, \
                f"Expected theme '{expected}' not found in '{dream_text}'. Found: {result.themes}"
    
    @pytest.mark.parametrize("dream_text,expected_themes", EN_THEME_CASES)
    def test_english_theme_detection(self, extractor, dream_text: str, expected_themes: List[str]):
        """Test English theme detection accuracy."""
        input_data = DreamInput(dream_text=dream_text, language="en")
        result = extractor.extract(input_data)
        
        for expected in expected_themes:
            assert expected in result.themes, \
                f"Expected theme '{expected}' not found in '{dream_text}'. Found: {result.themes}"
    
    def test_all_themes_supported(self, extractor):
        """Verify all defined themes are supported."""
        supported = extractor.get_supported_themes()
        
        for theme in THEMES:
            assert theme in supported, f"Theme '{theme}' should be supported"
    
    def test_theme_count(self, extractor):
        """Verify the expected number of themes."""
        supported = extractor.get_supported_themes()
        
        # Should have 15 themes
        assert len(supported) == 15, f"Expected 15 themes, got {len(supported)}"
    
    def test_theme_factor_matrix_format(self, extractor):
        """Test that theme factors follow the correct naming convention."""
        dream_text = "我梦见被人追赶，拼命逃跑"
        input_data = DreamInput(dream_text=dream_text, language="zh")
        result = extractor.extract(input_data)
        factor_matrix = result.to_factor_matrix()
        
        # Check that theme factors have correct prefix
        theme_factors = [f for f in factor_matrix.factors.keys() if f.startswith("dream_theme_")]
        
        assert len(theme_factors) > 0, "Should have at least one theme factor"
        
        for factor_id in theme_factors:
            # Factor ID should be dream_theme_{theme_name}
            parts = factor_id.split("_")
            assert len(parts) >= 3, f"Invalid theme factor format: {factor_id}"
            assert parts[0] == "dream", f"Factor should start with 'dream': {factor_id}"
            assert parts[1] == "theme", f"Factor should have 'theme' as second part: {factor_id}"
