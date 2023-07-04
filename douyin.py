# -*- coding: utf-8 -*-
# @Time     : 2023/7/4 21:25
# @Author   : HSJ
# @Software : PyCharm

import re
import sys

import requests

DEBUG = False

headers = {
    'host': 'live.douyin.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'cookie': 'ttwid=1%7CZ0iPSz8La8-_SDTQYp4gvCqvHYYC_hVuA6TTvx_ZCaM%7C1687964011%7Cc00a04ee0b83ff52c4ee556dec4c70aafc0332db13a45baeacef7f85abf04c7e; xgplayer_user_id=280967546384; ttcid=52f20544958043c0b455991d0bea411835; strategyABtestKey=%221688388439.659%22; passport_csrf_token=f151c0ca78a4161dd4b608b079125713; passport_csrf_token_default=f151c0ca78a4161dd4b608b079125713; __live_version__=%221.1.1.1011%22; SEARCH_RESULT_LIST_TYPE=%22single%22; download_guide=%223%2F20230703%2F0%22; pwa2=%220%7C0%7C3%7C0%22; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; s_v_web_id=verify_ljmvqnme_rI25qqgc_mq25_4CUI_9O6V_4jMH8fU4zsN9; n_mh=YXi_hzjAdamGa6X-5tV2Sg-cFozFj66hKkmKdrBxp5o; passport_auth_status=1259f4208c71d2c896ac7d8d76da95d6%2C; passport_auth_status_ss=1259f4208c71d2c896ac7d8d76da95d6%2C; publish_badge_show_info=%220%2C0%2C0%2C1688389904079%22; my_rd=1; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAH3UQ55HusNdQG6ydZQQNxkW1MSgEmgMg54e0ZELfdHo%2F1688400000000%2F0%2F1688390876340%2F0%22; store-region=cn-js; store-region-src=uid; LOGIN_STATUS=0; odin_tt=32254a7b0c9ad3ba2232992f0eb6ba487bc75af6e5b24e3115542124f3c5122df902062fb90c498b420214bb24c6169f80ab3d891494517d4c95a33f2b40b01c005b586e92d9e05df58da1057b791d32; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1689002569360%2C%22type%22%3Anull%7D; __ac_nonce=064a3f2490082503c3836; __ac_signature=_02B4Z6wo00f01F6GwNQAAIDBPYwAvVrYZ7BepsRAAHMJvZcNkMZyBWiNX8bM7gwyeYam6tNG1kSyN2m-lpRau3I2-SEuuxlmA3dOJdMEE4SPV-1w3xTIFTus78iSm2N3m9EOlU-MNa9x6x2R30; device_web_cpu_core=20; device_web_memory_size=8; webcast_local_quality=sd; csrf_session_id=d62696908df3e4ceb9144b4d1fec42b5; msToken=IOGZadaDm-QCgNU8ZLQcnBca6jrLoayKfOtt3j1kPAZnC-_L0F09X4v2ghVOBYarmH70B60eeUsIpDLs92FKT-8JSHi33wzUBRo53XfkgjzZNuxWdEarRQ==; tt_scid=WEZhSnUohcKVsAEwqD7-U6mnKwafdCnBmFjV7wvalDAu62c4BbzYesRzMR4DiADO102d; home_can_add_dy_2_desktop=%221%22; msToken=02cSUglI05BmuTZwWyBm7_QyOWNIU4j0uUfqd_Ftm5BidiLkH0hq5pxAY_sNT7fq3kbLW0RcOpuCdA3tm5qVmLiHPj4in-DCGSWYfDXJjYTjBzMIIb3fGA==; live_can_add_dy_2_desktop=%221%22',
}

url = input('请输入抖音直播链接：')
try:
    url = re.search(r'(https.*)', url).group(1)
    web_rid = re.search(r'(\d.*)',url).group(1)
    response = requests.get(url, headers=headers).text
    room_id = re.search(r'rlweWe(\d{19})', response).group(1)
except Exception as e:
    if DEBUG:
        print(e)
    print('获取room_id失败')
    sys.exit(1)
print('room_id', room_id)

try:
    params = (
        ('app_name', 'douyin_web'),
        ('live_id', '1'),
        ('room_id_str', room_id),
        ('aid', '6383'),
        ('device_platform','web'),
        ('enter_fro','web_search'),
        ('cookie_enabled','true'),
        ('browser_language','zh-CN'),
        ('browser_platform','Win32'),
        ('browser_name','Chrome'),
        ('browser_version','14.0.0.0'),
        ('web_rid',web_rid),
    )
    
    response = requests.get('https://live.douyin.com/webcast/room/web/enter/', headers=headers, params=params).json()
    hls_pull_url = response['data']['data'][0]['stream_url']['hls_pull_url']
    print(hls_pull_url)
    
except Exception as e:
    if DEBUG:
        print(e)
    print('获取real url失败')
