"""Build the English page (en.html) from the Chinese page (index.html)."""

from pathlib import Path
import re

root = Path(__file__).resolve().parent.parent
src = (root / 'index.html').read_text(encoding='utf-8')
R = [
# 先换整句提示，避免后面的按钮文字替换拆开它
('从 Gitee 下载。也可以从 GitHub 下载<a href="https://github.com/FuFu-Flash/EasyHub/releases/download/v1.4.0/EasyHub-1.4.0-setup.exe">安装版</a>或<a href="https://github.com/FuFu-Flash/EasyHub/releases/download/v1.4.0/EasyHub-1.4.0-portable.exe">便携版</a>，文件完全一样。', 'Also on Gitee: <a href="https://gitee.com/HUAJILA/easy-hub/releases/download/v1.4.0/EasyHub-1.4.0-setup.exe">installer</a> · <a href="https://gitee.com/HUAJILA/easy-hub/releases/download/v1.4.0/EasyHub-1.4.0-portable.exe">portable</a>. The files are identical.'),
('<html lang="zh-CN">', '<html lang="en">'),
("""  if(english){
    location.replace(new URL('en.html'+location.search+location.hash,location.href));
  }
""", ""),
('<title>EasyHub - 不会 Git 也能用的 GitHub 客户端</title>', '<title>EasyHub - A GitHub app you can use without knowing Git</title>'),
('content="EasyHub 是面向新手的开源 GitHub 客户端。在 Windows、macOS 上选文件夹、写一句说明就能发布源码；在 Android 上查看项目、回复问题、审查合并请求。"', 'content="EasyHub is an open source GitHub app for beginners. On Windows or macOS, pick a folder and write one line to publish your code. On Android, browse projects, reply to issues and review pull requests."'),
('<link rel="canonical" href="https://fufu-flash.github.io/easyhub-website/">', '<link rel="canonical" href="https://fufu-flash.github.io/easyhub-website/en.html">'),
('content="zh_CN"', 'content="en_US"'),
('content="EasyHub - 不会 Git 也能用的 GitHub 客户端"', 'content="EasyHub - A GitHub app you can use without knowing Git"'),
('content="选文件夹、写一句说明，就能把作品发布到 GitHub。支持 Windows、macOS 与 Android，免费开源。"', 'content="Pick a folder, write one line, and your work is on GitHub. Free and open source for Windows, macOS and Android."'),
('<meta property="og:url" content="https://fufu-flash.github.io/easyhub-website/">', '<meta property="og:url" content="https://fufu-flash.github.io/easyhub-website/en.html">'),
('content="EasyHub：让 GitHub 简单到每个人都会用"', 'content="EasyHub: GitHub made simple for everyone"'),
('"面向新手的开源 GitHub 客户端：不装 Git 也能发布源码、发布新版本、处理问题和合并请求。"', '"An open source GitHub app for beginners: publish code and releases, and handle issues and pull requests without installing Git."'),
('"url": "https://fufu-flash.github.io/easyhub-website/",', '"url": "https://fufu-flash.github.io/easyhub-website/en.html",'),
('app-home-zh.png', 'app-home-en.png'),
('"url": "https://fufu-flash.github.io/easyhub-website/#download"', '"url": "https://fufu-flash.github.io/easyhub-website/en.html#download"'),
('"Apple 芯片 Mac 上的开源 GitHub 客户端，用于发布和管理项目。"', '"An open source GitHub app for Apple silicon Macs to publish and manage projects."'),
('"url": "https://fufu-flash.github.io/easyhub-website/android.html"', '"url": "https://fufu-flash.github.io/easyhub-website/android-en.html"'),
('"在 Android 上查看 GitHub 项目、回复问题、下载发行版和审查合并请求。"', '"Browse GitHub projects, reply to issues, download releases and review pull requests on Android."'),
('"downloadUrl": "https://gitee.com/HUAJILA/easy-hub/releases/download/macos-v1.2.2/EasyHub-macOS.dmg"', '"downloadUrl": "https://github.com/FuFu-Flash/EasyHub/releases/download/macos-v1.2.2/EasyHub-macOS.dmg"'),
('"downloadUrl": "https://gitee.com/HUAJILA/easy-hub/releases/download/android-v1.1.0/EasyHub-Android-1.1.0-arm64.apk"', '"downloadUrl": "https://github.com/FuFu-Flash/EasyHub/releases/download/android-v1.1.0/EasyHub-Android-1.1.0-arm64.apk"'),
('跳到正文', 'Skip to content'),
('aria-label="页面导航"', 'aria-label="Page sections"'),
('>功能</a>', '>Features</a>'), ('>怎么用</a>', '>How it works</a>'),
('href="android.html">Android 版</a>', 'href="android-en.html">Android</a>'), ('>下载</a>', '>Download</a>'),
('aria-label="在 GitHub 查看源码" title="在 GitHub 查看源码"', 'aria-label="View source on GitHub" title="View source on GitHub"'),
('aria-label="切换到深色模式" title="切换到深色模式"', 'aria-label="Switch to dark mode" title="Switch to dark mode"'),
('<a href="./" data-lang="zh" lang="zh-CN" aria-current="page">中文</a>', '<a href="./" data-lang="zh" lang="zh-CN">中文</a>'),
('<a href="en.html" data-lang="en" lang="en">EN</a>', '<a href="en.html" data-lang="en" lang="en" aria-current="page">EN</a>'),
('<h1>不会 Git，也能把作品发到 GitHub</h1>', '<h1>Put your work on GitHub, no Git required</h1>'),
('EasyHub 是面向新手的 GitHub 客户端。选一个文件夹，写一句“这次改了什么”，点一下就发布。问题、合并请求和新版本也都在同一个地方处理。', 'EasyHub is a GitHub app for beginners. Pick a folder, write a line about what changed, and publish with one click. Issues, pull requests and releases live in the same place.'),
('免费下载', 'Download free'), ('>查看源码</a>', '>View source</a>'),
('<span>不用装 Git</span>', '<span>No Git install</span>'), ('<span>Apache-2.0 开源</span>', '<span>Apache-2.0 open source</span>'),
('alt="EasyHub 1.4.0 首页：左侧是导航，中间是“等你处理”和“我的项目”列表，右侧是最近更新"', 'alt="EasyHub 1.4.0 home: navigation on the left, Waiting for you and My projects in the middle, Recent updates on the right"'),
('<p class="section-label">功能</p>', '<p class="section-label">Features</p>'),
('日常要做的事，都变成了按钮', 'Everyday GitHub tasks, turned into buttons'),
('<h3>选文件夹就能发布</h3>', '<h3>Publish from a folder</h3>'),
('自动找出新增、修改和删除的文件。勾选这次要发的改动，写一句说明，点“发布源码”。没勾选的继续留在电脑上。', 'EasyHub finds added, changed and deleted files. Tick what to include, write a short note and click Publish code. Anything you leave unticked stays on your computer.'),
('<h3>不会悄悄覆盖文件</h3>', '<h3>Nothing gets overwritten quietly</h3>'),
('发布前先看看 GitHub 上有没有新内容。同一个文件两边都改过时，会把两个版本摆出来，让你选留哪个。', 'Before publishing, EasyHub checks GitHub for newer changes. If the same file changed in both places, you see both versions and choose which to keep.'),
('<h3>发布新版本</h3>', '<h3>Publish releases</h3>'),
('写好版本号和介绍，附上安装包等下载文件。可以先预览，确认后再发布；没写完的下次接着写。', 'Add a version number, notes and download files such as installers. Preview before you publish, and pick up unfinished drafts later.'),
('<h3>问题和合并请求</h3>', '<h3>Issues and pull requests</h3>'),
('首页“等你处理”列出待回复的问题和待审查的合并请求。看完改了什么，再决定合入还是关闭。', 'Waiting for you on the home page lists issues to answer and pull requests to review. See what changed, then merge or close.'),
('<h3>AI 帮你看改动<span class="tag">可选</span></h3>', '<h3>AI review<span class="tag">Optional</span></h3>'),
('填上自己的 API Key，AI 会总结改了什么、指出可能的问题。发送前先告诉你要发什么，合不合入还是你说了算。', 'Add your own API key and AI summarizes changes and flags possible problems. You see what will be sent first, and the final call is always yours.'),
('<h3>发现好项目</h3>', '<h3>Discover projects</h3>'),
('搜索公开项目和用户，看看今天、本周的 EasyHub 热门。英文介绍和问题可以一键翻译成中文。', 'Search public projects and people, and browse EasyHub Trending for today or this week. Translate READMEs and issues with one click.'),
('<p class="section-label">怎么用</p>', '<p class="section-label">How it works</p>'),
('三步发布第一个作品', 'Publish your first project in three steps'),
('<h3>用 GitHub 登录</h3>', '<h3>Sign in with GitHub</h3>'),
('在浏览器里完成授权就行，不用另外注册 EasyHub 账号。', 'Approve access in your browser. No separate EasyHub account needed.'),
('<h3>选择项目</h3>', '<h3>Choose a project</h3>'),
('添加电脑上已有的文件夹，下载自己在 GitHub 上的项目，或者新建一个。', 'Add a folder you already have, download one of your GitHub projects, or start a new one.'),
('<h3>写一句说明，发布</h3>', '<h3>Write a note and publish</h3>'),
('看看改了哪些文件，写下这次改了什么，点“发布源码”。', 'Check which files changed, describe the update and click Publish code.'),
('还没准备好登录？先打开模拟项目随便点点，不会上传到 GitHub。', 'Not ready to sign in? Try the demo project first. Nothing is uploaded to GitHub.'),
('<p class="section-label">下载</p>', '<p class="section-label">Download</p>'),
('选择你的设备', 'Choose your device'),
('全部免费。桌面版负责创作和发布，Android 版适合随时查看项目、回复问题和审查合并请求。', 'Free on every platform. Use the desktop app to create and publish, and Android to check projects, reply to issues and review pull requests on the go.'),
('<span>平台</span><span>适用于</span>', '<span>Platform</span><span>Requirements</span>'),
('1.4.0 · 全新界面', '1.4.0 · New look'),
('<b>64 位 Windows</b><br>安装版约 83 MB，便携版下载后直接运行', '<b>64-bit Windows</b><br>Installer about 83 MB; the portable version runs without installing'),
('>下载安装版</a>', '>Download installer</a>'), ('>便携版</a>', '>Portable</a>'),
('<b>Apple 芯片 Mac</b><br>macOS 12 及以上，DMG 约 70 MB', '<b>Apple silicon Mac</b><br>macOS 12 or later, DMG about 70 MB'),
('还没有经过 Apple 公证，第一次打开会被拦下，按 <a href="https://github.com/FuFu-Flash/EasyHub#macos-%E5%BF%85%E7%9C%8B" target="_blank" rel="noopener noreferrer">安装说明</a> 允许即可。', 'Not yet notarized by Apple, so macOS blocks the first launch. Follow the <a href="https://github.com/FuFu-Flash/EasyHub/blob/main/README.en.md" target="_blank" rel="noopener noreferrer">install guide</a> to allow it.'),
('1.1.0 · <a href="android.html">了解 Android 版</a>', '1.1.0 · <a href="android-en.html">About the Android app</a>'),
('<b>Android 7.0 及以上</b><br>适合大多数手机的精简安装包，约 26 MB', '<b>Android 7.0 or later</b><br>Compact package for most phones, about 26 MB'),
('装不上时换成通用安装包（<a href="https://gitee.com/HUAJILA/easy-hub/releases/download/android-v1.1.0/EasyHub-Android-1.1.0-universal.apk">Gitee</a> · <a href="https://github.com/FuFu-Flash/EasyHub/releases/download/android-v1.1.0/EasyHub-Android-1.1.0-universal.apk">GitHub</a>）。手机上不能发布源码，发布请用桌面版。', 'If it does not install, use the universal package (<a href="https://github.com/FuFu-Flash/EasyHub/releases/download/android-v1.1.0/EasyHub-Android-1.1.0-universal.apk">GitHub</a> · <a href="https://gitee.com/HUAJILA/easy-hub/releases/download/android-v1.1.0/EasyHub-Android-1.1.0-universal.apk">Gitee</a>). Publishing code needs the desktop app.'),
('Windows 版还没有购买代码签名，第一次运行可能提示“未知发布者”。', 'The Windows app is not code-signed yet, so the first launch may show "Unknown publisher".'),
('历史版本和 macOS 的 ZIP 包在 <a href="https://github.com/FuFu-Flash/EasyHub/releases" target="_blank" rel="noopener noreferrer">GitHub 发布页</a> 和 <a href="https://gitee.com/HUAJILA/easy-hub/releases" target="_blank" rel="noopener noreferrer">Gitee 发布页</a>。', 'Older versions and the macOS ZIP are on the <a href="https://github.com/FuFu-Flash/EasyHub/releases" target="_blank" rel="noopener noreferrer">GitHub releases page</a> and the <a href="https://gitee.com/HUAJILA/easy-hub/releases" target="_blank" rel="noopener noreferrer">Gitee releases page</a>.'),
('<span>Apache-2.0 开源 · 使用 GitHub 账号登录，没有自己的服务器</span>', '<span>Apache-2.0 open source · Signs in with your GitHub account, no EasyHub servers</span>'),
('aria-label="外部链接"', 'aria-label="Links"'), ('>反馈问题</a>', '>Report an issue</a>'),
]
for a, b in R:
    if a not in src:
        print('MISSING', a[:60])
    src = src.replace(a, b)
# English visitors get GitHub links first; the Chinese page leads with Gitee
for name in ['EasyHub-1.4.0-setup.exe', 'EasyHub-1.4.0-portable.exe']:
    button = f'btn-sm" href="https://gitee.com/HUAJILA/easy-hub/releases/download/v1.4.0/{name}"'
    assert button in src, name
    src = src.replace(button, f'btn-sm" href="https://github.com/FuFu-Flash/EasyHub/releases/download/v1.4.0/{name}"')
src = src.replace('"downloadUrl": "https://gitee.com/HUAJILA/easy-hub/releases/download/v1.4.0/', '"downloadUrl": "https://github.com/FuFu-Flash/EasyHub/releases/download/v1.4.0/')
for plat in ['macos-v1.2.2/EasyHub-macOS.dmg', 'android-v1.1.0/EasyHub-Android-1.1.0-arm64.apk']:
    gitee = f'<a class="btn btn-primary btn-sm" href="https://gitee.com/HUAJILA/easy-hub/releases/download/{plat}">从 Gitee 下载</a>'
    gh = f'<a class="btn btn-secondary btn-sm" href="https://github.com/FuFu-Flash/EasyHub/releases/download/{plat}">从 GitHub 下载</a>'
    pair = gitee + '\n          ' + gh
    assert pair in src, plat
    src = src.replace(pair, f'<a class="btn btn-primary btn-sm" href="https://github.com/FuFu-Flash/EasyHub/releases/download/{plat}">Download from GitHub</a>\n          <a class="btn btn-secondary btn-sm" href="https://gitee.com/HUAJILA/easy-hub/releases/download/{plat}">From Gitee</a>')
(root / 'en.html').write_text(src, encoding='utf-8')
leftover = [m for m in re.findall(r'[一-鿿][^<>"]*', src) if m not in ('中文', '语言 / Language')]
if leftover:
    raise SystemExit(f'Untranslated text: {leftover}')
