import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  lang: 'zh-CN',
  description: "又一个 Clash 订阅转换",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: nav(),
    sidebar: {
      'zh_CN/guide/': sidebarGuide()
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/Geniucker/sub-conv' }
    ],
    editLink: {
      pattern: 'https://github.com/Geniucker/sub-conv/edit/main/docs/:path'
    },
    search: {
      provider: 'local'
    },
    footer: {
      message: '在 MIT 许可证下发布。',
      copyright: 'Copyright © 2022-现在 <a href="https://github.com/Geniucker" target="_blank">@Geniucker</a>'
    }
  }
})


function nav() {
  return [
    { text: '首页', link: '/zh_CN/' },
    { text: '指南', link: '/zh_CN/guide/introduction/what-is-sub-conv'},
    { text: 'GitHub', link: 'https://github.com/Geniucker/sub-conv'}
  ]
}

function sidebarGuide() {
  return [
    {
      text: '简介',
      collapsed: false,
      items: [
        { text: '什么是 sub-conv', link: '../introduction/what-is-sub-conv' },
        { text: '为什么使用 sub-conv', link: '../introduction/why-sub-conv' },
        { text: '开始使用', link: '../introduction/getting-started' }
      ]
    },
    {
      text: '部署',
      collapsed: false,
      items: [
        { text: '在 Vercel 上部署', link: '../deploy/vercel' },
        { text: '在 VPS 或 PC 上部署', link: '../deploy/vps' }
      ]
    },
    {
      text: '配置',
      collapsed: false,
      items: [
        { text: '规则集', link: '../configuration/rule-set' },
        { text: 'Proxy Groups', link: '../configuration/proxy-groups' },
        { text: '规则自动缓存', link: '../configuration/cache' }
      ]
    },
    {
      text: '高级用法',
      collapsed: false,
      items: [
        { text: 'APIs', link: '../advanced-usage/apis' }
      ]
    }

  ]
}