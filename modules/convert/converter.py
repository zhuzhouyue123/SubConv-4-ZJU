

from modules.convert.util import RandUserAgent
from modules.convert.util import get
from modules.convert.util import uniqueName
from modules.convert.util import urlSafe
from modules.convert.util import base64RawStdDecode
from modules.convert.util import base64RawURLDecode
from modules.convert.v import handleVShareLink

import json
import base64
import urllib.parse as urlparse
import distutils

def ConvertsV2Ray(buf):

    data = base64.b64decode(buf).decode("utf-8")

    arr = data.splitlines()

    proxies = []
    names = {}

    for line in arr:
        if line == "":
            continue
    
        if -1 == line.find("://"):
            continue
        else:
            scheme, body = line.split("://", 1)
        
        scheme = scheme.lower()
        if scheme == "hysteria":
            try:
                urlHysteria = urlparse.urlparse(line)
            except:
                continue

            query = dict(urlparse.parse_qsl(urlHysteria.query))
            name = uniqueName(names, urlparse.unquote(urlHysteria.fragment))
            hysteria = {}

            hysteria["name"] = name
            hysteria["type"] = scheme
            hysteria["server"] = urlHysteria.hostname
            hysteria["port"] = urlHysteria.port
            hysteria["sni"] = query.get("peer")
            hysteria["obfs"] = query.get("obfs")
            hysteria["alpn"] = str(query.get("alpn"))
            hysteria["auth_str"] = query.get("auth")
            hysteria["protocol"] = query.get("protocol")
            up = query.get("up")
            down = query.get("down")
            if up == "":
                up = query.get("upmbps")
            if down == "":
                down = query.get("downmbps")
            hysteria["up"] = up
            hysteria["down"] = down
            hysteria["skip-cert-verify"] = bool(distutils.util.strtobool(query.get("insecure")))

            proxies.append(hysteria)
        elif scheme == "trojan":
            try:
                urlTrojan = urlparse.urlparse(line)
            except:
                continue

            query = dict(urlparse.parse_qsl(urlTrojan.query))

            name = uniqueName(names, urlparse.unquote(urlTrojan.fragment))
            trojan = {}

            trojan["name"] = name
            trojan["type"] = scheme
            trojan["server"] = urlTrojan.hostname
            trojan["port"] = urlTrojan.port
            trojan["password"] = urlTrojan.password
            trojan["udp"] = True
            trojan["skip-cert-verify"] = bool(distutils.util.strtobool(query.get("allowInsecure")))

            sni = get(query.get("sni"))
            if sni != "":
                trojan["sni"] = sni

            network = get(query.get("type").lower())
            if network != "":
                trojan["network"] = network
            
            if network == "ws":
                headers = {}
                wsOpts = {}

                headers["User-Agent"] = RandUserAgent()

                wsOpts["path"] = query.get("path")
                wsOpts["headers"] = headers

                trojan["ws-opts"] = wsOpts

            elif network == "grpc":
                grpcOpts = {}
                grpcOpts["serviceName"] = query.get("serviceName")
                trojan["grpc-opts"] = grpcOpts

            fingerprint = get(query.get("fp"))
            if fingerprint == "":
                trojan["client-fingerprint"] = "chrome"
            else:
                trojan["client-fingerprint"] = fingerprint
            
            proxies.append(trojan)
        
        elif scheme == "vless":
            try:
                urlVless = urlparse.urlparse(line)
            except:
                continue

            query = dict(urlparse.parse_qsl(urlVless.query))
            vless = {}
            try:
                handleVShareLink(names, urlVless, scheme, vless)
            except:
                continue
            flow = get(query.get("flow"))
            if flow != "":
                vless["flow"] = str(flow).lower()
            proxies.append(vless)

        elif scheme == "vmess":
            try:
                dcBuf = base64.b64decode(body)
            except:
                # Xray VMessAEAD share link
                try:
                    urlVMess = urlparse.urlparse(line)
                except:
                    continue
                query = dict(urlparse.parse_qsl(urlVMess.query))
                vmess = {}
                try:
                    handleVShareLink(names, urlVMess, scheme, vmess)
                except:
                    continue
                vmess["alterId"] = 0
                vmess["cipher"] = "auto"
                encryption = get(query.get("encryption"))
                if encryption != "":
                    vmess["cipher"] = encryption
                proxies.append(vmess)
                continue

            try:
                jsonDc = json.loads(dcBuf)
            except:
                continue
            values = {}
            
            try:
                tempName = values["ps"]
            except:
                continue
            name = uniqueName(names, tempName)
            vmess = {}

            vmess["name"] = name
            vmess["type"] = scheme
            vmess["server"] = values["add"]
            vmess["port"] = values["port"]
            vmess["uuid"] = values["id"]
            alterId = values.get("aid")
            if alterId is not None:
                vmess["alterId"] = alterId
            else:
                vmess["alterId"] = 0
            vmess["udp"] = True
            vmess["xudp"] = True
            vmess["tls"] = False
            vmess["skip-cert-verify"] = False

            vmess["cipher"] = "auto"
            cipher = get(values.get("scy"))
            if cipher != "":
                vmess["cipher"] = cipher

            sni = get(values.get("sni"))
            if sni != "":
                vmess["servername"] = sni
            
            network = get(values.get("net")).lower()
            if values["type"] == "http":
                network = "http"
            elif network == "http":
                network = "h2"
            vmess["network"] = network

            tls = values.get("tls")
            if tls is not None:
                tls = str(tls).lower()
                if tls.endswith("tls"):
                    vmess["tls"] = True

            if network == "http":
                headers = {}
                httpOpts = {}
                host = get(values.get("host"))
                if host != "":
                    headers["Host"] = host
                httpOpts["path"] = "/"
                path = get(values.get("path"))
                if path != "":
                    httpOpts["path"] = path
                httpOpts["headers"] = headers

                vmess["http-opts"] = httpOpts
            
            elif network == "h2":
                headers = {}
                h2Opts = {}
                host = get(values.get("host"))
                if host != "":
                    headers["Host"] = host
                h2Opts["path"] = get(values.get("path"))
                h2Opts["headers"] = headers

                vmess["h2-opts"] = h2Opts

            elif network == "ws":
                headers = {}
                wsOpts = {}
                wsOpts["path"] = "/"
                host = get(values.get("host"))
                if host != "":
                    headers["Host"] = host
                path = get(values.get("path"))
                if path != "":
                    wsOpts["path"] = path
                wsOpts["headers"] = headers
                vmess["ws-opts"] = wsOpts

            elif network == "grpc":
                grpcOpts = {}
                grpcOpts["grpc-service-name"] = get(values.get("path"))
                vmess["grpc-opts"] = grpcOpts
            
            proxies.append(vmess)

        # ss and ssr still WIP
        elif scheme == "ss":
            try: 
                urlSS = urlparse.urlparse(line)
            except:
                continue

            name = uniqueName(names, urlparse.unquote(urlSS.fragment))
            port = urlSS.port

            if port == "":
                try:
                    dcBuf = base64RawStdDecode(urlSS.hostname)
                except:
                    continue

                try:
                    urlSS = urlparse.urlparse("ss://"+dcBuf)
                except:
                    continue
            
            # there may be bugs
            cipherRaw = urlSS.username
            cipher = cipherRaw
            password = urlSS.password
            if password is None:
                try:
                    dcBuf = base64RawStdDecode(cipherRaw)
                except:
                    try:
                        dcBuf = base64RawURLDecode(cipherRaw)
                    except:
                        continue
                try:
                    cipher, password = dcBuf.split(":", 1)
                except:
                    continue
            # ther may be bugs

            ss = {}

            ss["name"] = name
            ss["type"] = scheme
            ss["server"] = urlSS.hostname
            ss["port"] = urlSS.port
            ss["cipher"] = cipher
            ss["password"] = password
            query = dict(urlparse.parse_qsl(urlSS.query))
            ss["udp"] = True
            if get(query.get("udp-over-tcp")) == "true" or get(query.get("uot")) == "1":
                ss["udp"] = True
            if "obfs" in get(query.get("plugin")):
                obfsParam = get(query.get("plugin-opts")).split(";")
                ss["plugin"] = "obfs"
                ss["plugin-opts"] = {
                    "host": obfsParam[2][10:],
                    "mode": obfsParam[1][5:],
                }
            proxies.append(ss)

        elif scheme == "ssr":
            try:
                dcBuf = base64RawStdDecode(body)
            except:
                continue

            try:
                before, after = dcBuf.split("/?", 1)
            except:
                continue

            beforeArr = before.split(":")

            if len(beforeArr) < 6:
                continue

            host = beforeArr[0]
            port = beforeArr[1]
            protocol = beforeArr[2]
            method = beforeArr[3]
            obfs = beforeArr[4]
            password = base64RawURLDecode(urlSafe(beforeArr[5]))

            try:
                query = dict(urlparse.parse_qsl(urlSafe(after)))
            except:
                continue

            remarks = base64RawURLDecode(query.get("remarks"))
            name = uniqueName(names, remarks)

            obfsParam = get(query.get("obfsparam"))
            protocolParam = get(query.get("protoparam"))

            ssr = {}

            ssr["name"] = name
            ssr["type"] = scheme
            ssr["server"] = host
            ssr["port"] = port
            ssr["cipher"] = method
            ssr["password"] = password
            ssr["protocol"] = protocol
            ssr["udp"] = True

            if obfsParam != "":
                ssr["obfs-param"] = obfsParam

            if protocolParam != "":
                ssr["protocol-param"] = protocolParam
            
            proxies.append(ssr)


    if len(proxies) == 0:
        raise Exception("No valid proxies found")

    return proxies


