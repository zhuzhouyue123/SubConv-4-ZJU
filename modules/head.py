"""
This module contains the components of the config of Clash
"""


HEAD = """mixed-port: 7890
allow-lan: true
mode: rule
log-level: info
external-controller: :9090
"""
PROVIDER_HEAD = """proxies:

proxy-providers:
  subscription:
    type: http
    url: {}
    interval: {}
    path: ./sub/subscription.yaml
    health-check:
      enable: true
      interval: 600
      # lazy: true
      url: http://www.gstatic.com/generate_204
"""
PROVIDER_BASE = """  {}:
    type: http
    url: {}
    interval: {}
    path: ./sub/subscription.yaml
    filter: "{}"
    health-check:
      enable: true
      interval: 600
      # lazy: true
      url: http://www.gstatic.com/generate_204
"""


PROXY_GROUP_HEAD = "proxy-groups:\n"
PROXY_GROUP_PROXY_SELECT = """  - name: 🚀 节点选择
    type: select
    proxies:
      - ♻️ 自动选择
      - 🔯 故障转移
      - 🔮 负载均衡
{}
      - 🚀 手动切换
      - DIRECT
"""
PROXY_GROUP_PROXY_MANUAL_SELECT = """  - name: 🚀 手动切换
    type: select
    use:
      - subscription
"""
PROXY_GROUP_PROXY_AUTO_SELECT = """  - name: ♻️ 自动选择
    type: url-test
    url: http://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    use:
      - subscription
"""
PROXY_GROUP_PROXY_FALLBACK = """  - name: 🔯 故障转移
    type: fallback
    url: http://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    use:
      - subscription
"""
PROXY_GROUP_PROXY_ANYCAST = """  - name: 🔮 负载均衡
    type: load-balance
    strategy: consistent-hashing
    url: http://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    use:
      - subscription
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
"""
PROXY_GROUP_REGION_GROUPS = """  - name: {}
    type: url-test
    url: http://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    use:
      - {}
"""
