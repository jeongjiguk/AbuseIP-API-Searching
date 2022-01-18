import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Solution(object):
   def validIPAddress(self, IP):
      """
      :type IP: str
      :rtype: str
      """
      def isIPv4(s):
         try: return str(int(s)) == s and 0 <= int(s) <= 255
         except: return False
      def isIPv6(s):
         if len(s) > 4:
            return False
         try : return int(s, 16) >= 0 and s[0] != '-'
         except:
            return False
      if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
         return "IPv4"
      if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")):
         return "IPv6"
      return "Neither"

def api_request(ip):
    url = 'https://api.abuseipdb.com/api/v2/check'
    
    querystring = {
        'ipAddress': ip,
        'maxAgeInDays': '90', 'verbose':''
        }

    headers = {
        'Accept': 'application/json',
        'Key': 'key입력'
        }

    response = requests.request(method='GET', url=url, headers=headers, params=querystring, verify=False)
    decodedResponse = json.loads(response.text)

    reports = decodedResponse['data']["reports"]

    a=[]
    catearr=[]
    str_cate=[]
    
    for i in reports:
        a = set(list(set(a))+(i['categories']))
    
    for j in a:
        if j==1:
            str_cate='DNS Compromise'
        elif j==2:
            str_cate='DNS Poisoning'
        elif j==3:
            str_cate='Fraud Orders'
        elif j==4:
            str_cate='DDoS Attack'
        elif j==5:
            str_cate='FTP Brute-Force'
        elif j==6:
            str_cate='Ping of Death'
        elif j==7:
            str_cate='Phishing'
        elif j==8:
            str_cate='Fraud VoIP'
        elif j==9:
            str_cate='Open Proxy'
        elif j==10:
            str_cate='Web Spam'
        elif j==11:
            str_cate='Email Spam'
        elif j==12:
            str_cate='Blog Spam'
        elif j==13:
            str_cate='VPN IP'
        elif j==14:
            str_cate='Port Scan'
        elif j==15:
            str_cate='Hacking'
        elif j==16:
            str_cate='SQL Injection'
        elif j==17:
            str_cate='Spoofing'
        elif j==18:
            str_cate='Brute-Force'
        elif j==19:
            str_cate='Bad Web Bot'
        elif j==20:
            str_cate='Exploited Host'
        elif j==21:
            str_cate='Web App Attack'
        elif j==22:
            str_cate='SSH'
        elif j==23:
            str_cate='IoT Targeted'
        catearr.append(str_cate)    
        

    result_dict = {
            'ipAddress': decodedResponse['data']["ipAddress"],
            'domain': decodedResponse['data']["domain"],
            'countryName' : decodedResponse['data']["countryName"],
            'category': catearr,
            }

    return result_dict


if __name__ == "__main__":
    
    ip = input("IP 입력: ").split()
    temp = []
    
    for i in ip:
        ob = Solution()
        check = str(ob.validIPAddress(i))
        if check == "Neither":
            print("=====================================")
            print(i+"는 잘못된 유형의 IP입니다.")
            print("=====================================")
            continue
        
        else:
            temp.append(api_request(i))
        
for i in temp:
     print("=====================================")
     print("IP 정보: ", i['ipAddress'])
     print("도메인 정보: ", i['domain'])
     print("국가 정보: ", i['countryName'])
     print("카테고리: ", i['category'])
     print("=====================================")

