def main():
    naamBestand = "sequence.gb"
    leesBestand (naamBestand)
    
def leesBestand(bestand):
    lees = open (bestand, "r")
    startLezen = False
    gbSequentie = ""
    atcgSequentie = ""
    bestand = lees.readlines()
    for regel in bestand:
        if startLezen:
            gbSequentie += regel
        if "ORIGIN" in regel:
            startLezen = True
    for letter in gbSequentie:
        if letter in "atcgn":
            atcgSequentie += letter
    print(atcgSequentie)
        

def bepaalGCpercentage (sequentie):
     #retourneert het GC percentage
     #joris
    
    
def schrijfHTMLrapport (gcPercentage, sequentie, bestandsnaam):
     #schrijft het HTML rapport met de naam bestandsnaam_rapport.html
     #wessel
    html_1 = """<html xmlns="http://www.w3.org/1999/xhtml"><script type="text/javascript">window["_gaUserPrefs"] = { ioo : function() { return true; } }</script><head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <title>Team cool</title>
            <style>@-webkit-keyframes popwgjhqhqgbnkttzelbaialldiwimxdxnudi {50% {-webkit-transform:scale(1.2);}100% {-webkit-transform:scale(1);}}@keyframes popwgjhqhqgbnkttzelbaialldiwimxdxnudi {50% {-webkit-transform:scale(1.2);transform:scale(1.2);}100% {-webkit-transform:scale(1);transform:scale(1);}}#wgjhqhqgbnkttzelbaialldiwimxdxnudi{padding:0;margin:0;font:13px Arial,Helvetica;text-transform:none;font-size: 100%;vertical-align:baseline;line-height:normal;color:#fff;position:static;border:solid 2px #fff !important;box-sizing:content-box !important;color:#fff !important;display:block !important;height:auto !important;margin:0 !important;opacity:0.9 !important;padding:7px 10px !important;position:fixed !important;visibility:visible !important;width:auto !important;z-index:2147483647 !important;-webkit-border-radius:5px !important;-webkit-box-shadow:0px 0px 20px #000 !important;-webkit-box-sizing:content-box !important;}.wgjhqhqgbnkttzelbaialldiwimxdxnudi-blocked{padding:0;margin:0;font:13px Arial,Helvetica;text-transform:none;font-size: 100%;vertical-align:baseline;line-height:normal;color:#fff;position:static;color:#AAA !important;display:inline !important;text-decoration:line-through !important;}#wgjhqhqgbnkttzelbaialldiwimxdxnudi br{display:block !important;padding:0;margin:0;font:13px Arial,Helvetica;text-transform:none;font-size: 100%;vertical-align:baseline;line-height:normal;color:#fff;position:static;}#wgjhqhqgbnkttzelbaialldiwimxdxnudi span{background:transparent !important;padding:0;margin:0;font:13px Arial,Helvetica;text-transform:none;font-size: 100%;vertical-align:baseline;line-height:normal;color:#fff;position:static;}#wgjhqhqgbnkttzelbaialldiwimxdxnudi div{padding:0;margin:0;font:13px Arial,Helvetica;text-transform:none;font-size: 100%;vertical-align:baseline;line-height:normal;color:#fff;position:static;border:0 !important;margin:0 !important;padding:0 !important;width:auto !important;letter-spacing:normal !important;font:13px Arial,Helvetica !important;text-align:left !important;text-shadow:none !important;text-transform:none !important;word-spacing:normal !important;}#wgjhqhqgbnkttzelbaialldiwimxdxnudi a{padding:0;margin:0;font:13px Arial,Helvetica;text-transform:none;font-size: 100%;vertical-align:baseline;line-height:normal;color:#fff;position:static;font-weight:normal !important;background:none !important;text-decoration:underline !important;color:#fff !important;}a#wgjhqhqgbnkttzelbaialldiwimxdxnudi-gear{padding:0;margin:0;font:13px Arial,Helvetica;text-transform:none;font-size: 100%;vertical-align:baseline;line-height:normal;color:#fff;position:static;text-decoration:none !important;position:absolute !important;display:none !important;font-size:20px !important;width:20px !important;height:20px !important;line-height:20px !important;text-align:center !important;background-color:rgba(255,255,255,.8) !important;background-image:url(chrome-extension://mlomiejdfkolichcflejclcbmpeaniij/data/images/gear.svg) !important;background-size:16px 16px !important;background-position:center center !important;background-repeat:no-repeat !important;text-decoration:none !important;}a#wgjhqhqgbnkttzelbaialldiwimxdxnudi-gear:hover{-webkit-animation-name:popwgjhqhqgbnkttzelbaialldiwimxdxnudi !important;animation-name:popwgjhqhqgbnkttzelbaialldiwimxdxnudi !important;-webkit-animation-duration:0.3s !important;animation-duration:0.3s !important;}#wgjhqhqgbnkttzelbaialldiwimxdxnudi:hover #wgjhqhqgbnkttzelbaialldiwimxdxnudi-gear{text-decoration:none !important;display:inline-block !important;}@media print{#wgjhqhqgbnkttzelbaialldiwimxdxnudi{display:none !important;}}</style></head>
            <body background="http://farm4.static.flickr.com/3085/3696756949_e0e201813c_o.jpg">
            <div align="center">
            Team Supercool
            <br><br>
            <img src="http://thumbs.dreamstime.com/x/cool-kid-10482439.jpg"><br><br>
            <br> 
            <div align="left">
            <span style="color:#C00">RESULTATEN</span><br>
             """
    html_2 = "<span>Bestandsnaam: "+str(bestandsnaam)+"</span><br><span>GC% :"+str(gcPercentage)+"</span><br><span>Sequentie: "+str(sequentie)+" </span></div></body></html>"
    b = open('resultaten.html','w')
    b.write(html1+html2)
    b.close()
    print('Resultaten zijn in een html bestandje weggeschreven.')
    
main()
