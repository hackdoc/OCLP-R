#!/usr/bin/env python3

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'oclp_r'))

from oclp_r.support import translate_language
from oclp_r import constants

# 创建一个模拟的常量对象
class MockConstants:
    def __init__(self):
        self.patcher_version = "1.0.0"
        self.detected_os = "macOS"
        self.detected_os_build = "22A"
        self.detected_os_version = "13.0"

# 测试翻译功能
def test_translation():
    print("=== 测试翻译功能 ===")
    
    # 创建翻译对象
    mock_constants = MockConstants()
    translator = translate_language.TranslateLanguage_sys_patch(mock_constants)
    
    # 测试 utilities 方法
    print("\n1. 测试 utilities 方法:")
    utilities_trans = translator.utilities()
    
    # 测试一些关键字符串
    test_strings = [
        "- Merging KDK with Root Volume: {kdk_name}",
        "- Successfully merged KDK with Root Volume", 
        "Failed to install KDK",
        "Unable to get KDK info: {error_msg}",
        "- Unable to find Kernel Debug Kit"
    ]
    
    for string in test_strings:
        if string in utilities_trans:
            print(f"✓ '{string}' -> '{utilities_trans[string]}'")
        else:
            print(f"✗ '{string}' 未找到")
    
    # 测试格式化字符串
    print("\n2. 测试格式化字符串:")
    test_string = "- Merging KDK with Root Volume: {kdk_name}"
    if test_string in utilities_trans:
        formatted = utilities_trans[test_string].format(kdk_name="TestKDK")
        print(f"✓ 格式化: '{formatted}'")
    
    # 测试错误消息
    print("\n3. 测试错误消息:")
    error_string = "Unable to get KDK info: {error_msg}"
    if error_string in utilities_trans:
        formatted_error = utilities_trans[error_string].format(error_msg="网络连接失败")
        print(f"✓ 错误消息: '{formatted_error}'")
    
    print("\n=== 测试完成 ===")

if __name__ == "__main__":
    test_translation()