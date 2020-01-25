import urllib.request
import os
def main():
 mac=input("Enter MAC:")
 mac=mac.replace(":","")
 #http://mobile.maps.yandex.net/cellid_location/?clid=1866854&lac=-1&cellid=-1&operatorid=null&countrycode=null&signalstrength=-1&wifinetworks=:-65&app=ymetro
 find(mac)
def find(mac):
 link="http://mobile.maps.yandex.net/cellid_location/?clid=1866854&lac=-1&cellid=-1&operatorid=null&countrycode=null&signalstrength=-1&wifinetworks="+mac+":-65&app=ymetro"
 try:
  page = urllib.request.urlopen(link)
  out=page.read()
 except:
  print("ERROR or Not found")
  exit(0)
 out=str(out)
 out=out[out.find("la"):out.find("nl")]
 out=out.replace("b'","")
 print("Location found:"+out)
main()
