"""
This module contains the components of the config of Clash
"""


HEAD = """mixed-port: 7890
allow-lan: true
mode: rule
log-level: info
external-controller: :9090
"""
DNS = """dns:
  enable: true
  listen: 0.0.0.0:1053
  default-nameserver:
    - 223.5.5.5
    - 8.8.8.8
    - 1.1.1.1
  nameserver:
    - "https://223.5.5.5/dns-query"
    - "https://1.12.12.12/dns-query"
    - "https://8.8.8.8/dns-query"
"""

PROVIDER_HEAD = "proxy-providers:\n"
PROVIDER_BASE0 = """  subscription{}:
    type: http
    url: {}
    interval: {}
    path: ./sub/subscription{}.yaml
    health-check:
      enable: true
      interval: 60
      # lazy: true
      url: http://www.apple.com/library/test/success.html
"""
PROVIDER_BASE1 = """  {}:
    type: http
    url: {}
    interval: {}
    path: ./sub/subscription{}.yaml
    filter: "{}"
    health-check:
      enable: true
      interval: 60
      # lazy: true
      url: http://www.apple.com/library/test/success.html
"""


PROXY_GROUP_HEAD = "proxy-groups:\n"
PROXY_GROUP_PROXY_SELECT = """  - name: 🚀 节点选择
    type: select
    proxies:
      - ♻️ 自动选择
      - 🔯 故障转移
      - 🔮 负载均衡{}
      - 🚀 手动切换
      - DIRECT
"""
PROXY_GROUP_PROXY_MANUAL_SELECT = """  - name: 🚀 手动切换
    type: select
    use:
{}
"""
PROXY_GROUP_PROXY_AUTO_SELECT = """  - name: ♻️ 自动选择
    type: url-test
    url: http://www.apple.com/library/test/success.html
    interval: 60
    tolerance: 50
    use:
{}
"""
PROXY_GROUP_PROXY_FALLBACK = """  - name: 🔯 故障转移
    type: fallback
    url: http://www.apple.com/library/test/success.html
    interval: 60
    tolerance: 50
    use:
{}
"""
PROXY_GROUP_PROXY_ANYCAST = """  - name: {}
    type: load-balance
    strategy: consistent-hashing
    url: http://www.apple.com/library/test/success.html
    interval: 60
    tolerance: 50
    use:
{}
"""
PROXY_GROUP_PROXY_FIRST = """  - name: {}
    type: select
    proxies:
      - 🚀 节点选择
{}
      - 🚀 手动切换
      - DIRECT
"""
PROXY_GROUP_DIRECT_FIRST = """  - name: {}
    type: select
    proxies:
      - DIRECT
      - 🚀 节点选择
{}
      - 🚀 手动切换
"""
PROXY_GROUP_REJECT_FIRST = """  - name: {}
    type: select
    proxies:
      - REJECT
      - DIRECT
      - 🚀 节点选择
{}
      - 🚀 手动切换
"""
PROXY_GROUP_REGION_GROUPS = """  - name: {}
    type: url-test
    url: http://www.apple.com/library/test/success.html
    interval: 60
    tolerance: 50
    use:
{}
"""
