"""Build the English GitHub Pages page from the Chinese source page."""

from html import unescape
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / 'index.html'
OUTPUT = ROOT / 'en.html'

TEXT = {
    '中文': '中文',
    '特性': 'Features',
    '热门': 'Trending',
    '使用流程': 'How it works',
    '同类对比': 'Comparison',
    '开始使用': 'Get started',
    '开源源码 · Apache-2.0 · Windows、macOS 与 Android': 'Open source code · Apache-2.0 · Windows, macOS and Android',
    '让 GitHub': 'Make GitHub',
    '简单到每个人都会用': 'simple for everyone',
    '在桌面版（Windows / macOS）上选择项目文件夹、写一句更新说明，就能把作品保存到 GitHub。拿起 Android 手机，随时查看项目、回复问题和审查合并请求。': 'On Windows or macOS, choose a project folder and write a short note to save your work to GitHub. On Android, browse projects, reply to issues, and review pull requests wherever you are.',
    '下载': 'Download',
    '查看 Gitee 仓库': 'View Gitee repo',
    '查看 GitHub 仓库': 'View GitHub repo',
    '免装 Git，双击即用': 'No Git install. Just launch.',
    '安全登录，直连 GitHub': 'Secure sign-in, direct GitHub access',
    '中英双语': 'Chinese & English',
    '有 5 个文件还没发布': '5 files waiting to be published',
    'Minecraft Mod · 准备好后发布': 'Minecraft Mod · Publish when ready',
    '搜索项目/用户...': 'Search projects or people...',
    '你': 'Y',
    '首页': 'Home',
    '我的项目': 'My projects',
    '发现': 'Discover',
    '问题': 'Issues',
    '设置': 'Settings',
    '← 所有项目': '← All projects',
    '所有人': 'Public',
    '为冒险加一点新乐趣': 'A little more fun for every adventure',
    '发布更新': 'Publish update',
    '发布新版本': 'New release',
    '打开文件夹': 'Open folder',
    '项目介绍': 'About this project',
    '✎ 编辑介绍': '✎ Edit description',
    '记录模组想法、玩法和安装说明。': 'Ideas, gameplay, and installation notes for the mod.',
    '看看大家的反馈': 'See what people are saying',
    '查看问题 →': 'View issues →',
    '历史版本': 'History',
    '查看全部 →': 'View all →',
    '修复窗口缩放问题': 'Fixed window resizing',
    '· 修改了 5 个文件': '· Changed 5 files',
    '为什么做 EasyHub': 'Why EasyHub',
    'GitHub 不该只有"懂的人"才用得好': 'GitHub should be useful to everyone',
    '命令行看不懂': 'The command line feels daunting',
    'add、commit、merge、rebase，一连串概念；一个报错信息就足以让人卡住，更不敢随便按回车。': 'Commands like add, commit, merge, and rebase are a lot to learn. One error message can stop a new user in their tracks.',
    '选个文件夹、写句话、点一下就发布': 'Choose a folder, write a line, and publish',
    '官方客户端仍然复杂': 'The official client is still complex',
    'GitHub Desktop 聚焦提交与分支，默认你理解仓库、暂存区；也不集中处理问题、项目下载这些日常操作。': 'GitHub Desktop focuses on commits and branches. It assumes you know repositories and staging, while issues and downloads live elsewhere.',
    '首页式界面，操作像手机 App 一样直观': 'A familiar home screen with straightforward actions',
    '网页操作繁琐': 'The website feels too technical',
    'GitHub 网页功能很全，但按钮和菜单里有仓库、分支、提交等专业术语。想创建项目、更新文件或处理问题，新手常常不知道从哪里开始。': 'GitHub offers many features, but labels such as repository, branch, and commit assume prior knowledge. New users can struggle to find where to create a project, update files, or handle an issue.',
    '把操作说清楚：新建项目、发布源码、查看问题': 'Clear actions: create a project, publish code, view issues',
    '核心特性': 'Features',
    '把日常用到的 GitHub 操作，都做成简单按钮': 'Everyday GitHub tasks, made simple',
    '桌面版负责创作和发布，Android 版方便随时查看项目、处理问题和合并请求。两端通过 GitHub 获取内容，无需 EasyHub 账号或自有服务器。': 'Create and publish on desktop. Use Android to browse projects, handle issues, and review pull requests on the go. Both apps connect to GitHub with no separate EasyHub account or server.',
    'AI 辅助审查': 'AI assisted review',
    '项目介绍，边写边看': 'Write your project introduction with live preview',
    '在 Windows 上选择“编辑”“预览”或“边写边看”。支持 Markdown 和常见 HTML，图片、居中内容、表格和折叠内容都能预览；宽屏双栏，窄屏自动上下排列。': 'On Windows, choose Edit, Preview, or Live Preview. Combine Markdown with common HTML and preview images, centered content, tables, and expandable sections. The editor and preview sit side by side in wide windows and stack in narrow ones.',
    '先保存，准备好了再发布': 'Save first, publish when ready',
    '切换模式保留草稿，取消不改原介绍。保存后先更新本地，点击“发布源码”再同步到 GitHub；英文界面也保留作者撰写的原文。': 'Switching modes keeps your draft; Cancel leaves the original unchanged. Save updates the local copy, and Publish Source syncs it to GitHub. The English interface preserves the author’s original text.',
    '代码与程序文件，先看清楚再决定': 'Review code and program files before you decide',
    '收到合并请求时，AI 把文字修改和程序文件整理到同一份结果中。Windows 也能审查电脑上的程序文件，或发行版里的 EXE、DLL 附件。确认后才开始，决定始终由你作出。': 'For pull requests, AI brings text changes and program files into one review. On Windows, also review local program files or EXE and DLL release attachments. Reviews begin after confirmation; the decision stays yours.',
    '支持 API Key': 'Supports API keys',
    '确认后才发送': 'Sent only after confirmation',
    '可随时取消': 'Cancel at any time',
    '程序文件审查支持 Windows、macOS 与 Android，按需安装组件；不会启动被审查程序，原始程序文件不会发给 AI。结果仅供参考，服务商可能收费。': 'Program file reviews support Windows, macOS and Android, with components installed as needed. Reviewed programs are never launched and original files are not sent to AI. Results are advisory; provider fees may apply.',
    '合并请求审查': 'Pull Request Reviews',
    '由你决定': 'You decide',
    '审查内容': 'Review content',
    '文字修改与程序文件，集中查看': 'Text changes and program files, together',
    '查看可能的问题、相关文件和建议，也能确认哪些内容已检查。': 'See potential issues, related files, and suggestions, plus what was checked.',
    '建议仅供参考': 'Suggestions only',
    '拒绝': 'Reject',
    '批准': 'Approve',
    '使用 GitHub 安全登录': 'Secure GitHub sign-in',
    '通过 GitHub 设备授权登录，无需另建账号。桌面版和 Android 各自使用系统安全存储保存凭证；项目资料直接从 GitHub 获取。': 'Sign in through GitHub device authorization with no new account. Desktop and Android each keep credentials in secure device storage; project data comes directly from GitHub.',
    '本地文件夹发布源码': 'Publish from a local folder',
    '选择文件夹即可识别项目；也能指定位置，找回已连接到自己 GitHub 项目的文件夹。后台扫描新增、修改、删除和重命名的文件，遵守 .gitignore、避开依赖目录；无需安装 Git。': 'Choose a folder to make it a project, or search a location for folders already connected to your GitHub projects. Background scanning detects added, changed, deleted, and renamed files while respecting .gitignore and skipping dependency folders. No Git installation is required.',
    '冲突安全处理': 'Safe conflict handling',
    '发布前先检查云端：可安全衔接的更新自动先获取；双方改动同一文件时，双版本预览、逐个选择保留版本。复杂历史会阻止自动发布，绝不强制覆盖。': 'EasyHub checks GitHub before publishing. Compatible updates are fetched first; if the same file changed in two places, you can compare both versions and choose what to keep. Complex cases stop the publish instead of overwriting files.',
    '问题与合并请求审查': 'Issues and Pull Request Reviews',
    'Windows 和 Android 都能创建、回复、关闭或重新打开问题，也能在“合并请求审查”中查看修改；Windows 还能为其他项目准备并提交合并请求。': 'Create, reply to, close, or reopen issues on Windows and Android, and inspect changes in Pull Request Reviews. On Windows, also prepare and submit pull requests to other projects.',
    '发布新版本 Release': 'Publish downloadable releases',
    '正式版、Alpha、Beta 三种类型，自动建议并续号版本名；可插入链接与图片、选择多个下载文件，按 GitHub 公开限制校验（单文件小于 2 GiB、每版最多 1000 个、不可同名），随后真实创建 Release、逐个上传附件，已完成端到端验收。': 'Choose a stable, Alpha, or Beta release and get a suggested version number. Add links, images, and multiple downloads; EasyHub checks GitHub limits before creating the release and uploading each file.',
    '公开内容翻译': 'Translate public content',
    '一键统一翻译项目简介、README、问题与 Release 描述；README 按段落随滚动逐步翻译。私有项目不发送给第三方，项目名、版本号、文件名以占位符保护，译文本地缓存。': 'Translate public project summaries, READMEs, issues, and release notes with one switch. README paragraphs translate as you scroll. Private projects are not sent to the translation provider, and names, versions, and filenames stay intact.',
    '连接不畅，有办法处理': 'Help when GitHub will not connect',
    'Windows 的 GitHub 系统代理也适用于遵循系统代理设置的浏览器。复用已有代理、不覆盖配置，其他工具接管时让出；关闭或退出后恢复 EasyHub 改过的设置，其他网站保持原连接方式。': 'The Windows GitHub system proxy also works in browsers that use system proxy settings. It reuses existing proxies without overwriting their configuration and steps aside when another tool takes over. Turning it off or exiting restores settings changed by EasyHub; other websites keep their original connection method.',
    '通知和下载，一眼看清': 'Clear notifications and downloads',
    'Windows 通知显示未读条数，查看后清零，已有待办仍然保留。下载时可查看进度、速度和剩余时间，也能取消下载。': 'Windows notifications show the unread count and clear after viewing, while pending items stay available. Track download progress, speed, and time remaining, or cancel a download.',
    '发现好项目': 'Discover projects',
    '发现值得关注的公开项目': 'Discover public projects worth following',
    '在“发现 / 搜索”里浏览近期活跃、受关注的公开项目，也可粘贴 GitHub 项目地址直达项目页。EasyHub 结合 Star 数、近期活动和更新时间排列结果，帮你找到感兴趣的作品。': 'Browse active, well-liked public projects in Discover, or paste a GitHub project URL to open it directly. EasyHub ranks projects using stars, recent activity, and update time to help you find something interesting.',
    '切换今日热门、本周热门、本月热门，看看不同时间里的新发现。': 'Switch between daily, weekly, and monthly trends.',
    '卡片展示作者、语言、Star 数和 EasyHub 观察到的增长趋势。': 'See each author, language, star count, and growth trend.',
    '查看项目介绍、问题与历史版本，再选择想下载的文件。': 'Read project details, issues, and history before choosing what to download.',
    '这是 EasyHub 自己的热门排序，不是 GitHub 官方 Trending。右侧项目仅为界面示例，实际内容从 GitHub 获取。': 'This is EasyHub’s own ranking, not GitHub’s official Trending list. The projects shown here illustrate the interface; live results come from GitHub.',
    '发现更多作品': 'Discover more',
    '发现 / 搜索': 'Discover / Search',
    '看看大家最近在创作什么。': 'See what people have been making lately.',
    '项目搜索': 'Projects',
    '用户搜索': 'People',
    '搜索公开项目...': 'Search public projects...',
    'EasyHub 热门': 'EasyHub Trending',
    '刷新': 'Refresh',
    '今日热门': 'Today',
    '本周热门': 'This week',
    '本月热门': 'This month',
    '轻量的开源画板与协作工具': 'A lightweight open source canvas for collaboration',
    '增长观察中': 'Tracking growth',
    '把零散想法整理成清晰笔记': 'Turn scattered ideas into clear notes',
    '观察期 +12 Star': '+12 stars recently',
    '四步，把本地改动发布到 GitHub': 'Publish local changes in four steps',
    '不需要命令行，也不需要事先理解分支、暂存区等概念。': 'No command line or knowledge of branches and staging required.',
    '步骤 01': 'Step 01',
    '步骤 02': 'Step 02',
    '步骤 03': 'Step 03',
    '步骤 04': 'Step 04',
    '选择本地文件夹': 'Choose a local folder',
    '添加电脑上已有的文件夹并识别为项目，或把 GitHub 上的云端项目下载到指定位置。': 'Add an existing folder as a project, or download a GitHub project to a location you choose.',
    '自动检查改动': 'Review changes automatically',
    '独立 Worker 扫描文件的新增、修改与删除，遵守 .gitignore 并避开常见依赖目录。': 'A background worker detects added, changed, and deleted files while respecting .gitignore and skipping dependency folders.',
    '写说明、处理冲突': 'Write a note and review conflicts',
    '用一句话说明本次更新；若云端也有改动，逐文件对比并选择要保留的版本。': 'Describe your update in one sentence. If GitHub also changed, compare files and choose the version to keep.',
    '一键发布源码': 'Publish your code',
    '自动先拉取可衔接的远端更新，再把本地改动安全同步到 GitHub，完成后可查看历史版本。': 'EasyHub fetches compatible updates first, then safely publishes your changes to GitHub. You can review the result in History.',
    '同类项目对比': 'Compare tools',
    '查看完整功能对比': 'View the full feature comparison',
    '差别不在功能多少，而在为谁设计': 'Designed around the people who use it',
    '大多数 GitHub 工具默认你已经懂 Git。EasyHub 从第一次接触 GitHub 的人的视角出发：把操作做少、把话说直白，让新手也能看懂每一步。': 'Most GitHub tools assume you already know Git. EasyHub starts with the first-time user: fewer steps, clearer language, and a path you can understand.',
    '项目': 'Project',
    '平台内容浏览': 'Browse GitHub',
    'Issues 管理': 'Manage issues',
    '本地源码发布': 'Publish local code',
    '免安装 Git': 'No Git install',
    '中文与翻译': 'Languages & translation',
    '开源': 'Open source',
    '面向新手': 'Beginner friendly',
    '本项目 · Windows': 'This project · Windows',
    'GitHub 官方': 'Official GitHub app',
    '闭源 · 尚未发布': 'Closed source · Unreleased',
    'AGPL · 桌面/移动': 'AGPL · Desktop/mobile',
    '菜单栏通知': 'Menu bar notifications',
    'Android 客户端': 'Android app',
    '具备': 'Supported',
    '部分支持 / 仅限特定场景': 'Partial / limited',
    '不支持': 'Not supported',
    '不涉及': 'Not applicable',
    '为新手重新设计，而不是堆叠功能': 'Designed for beginners, with less to learn',
    'GitHub Desktop、GitKraken 等工具默认用户理解提交与分支；OctoPunk 明确面向 power user；DevHub、Gitify 只解决通知。EasyHub 把日常操作收进一个首页——': 'GitHub Desktop and GitKraken assume you know commits and branches. OctoPunk targets power users, while DevHub and Gitify focus on notifications. EasyHub brings everyday tasks into one home screen: ',
    '新建项目、看到改动、写一句话、点"发布更新"': 'create a project, see changes, write a short note, and publish',
    '；项目介绍、问题和历史版本也能在应用中查看。': '. You can also browse project details, issues, and history in the app.',
    '一句话定位': 'In one sentence',
    'EasyHub 不追求覆盖 GitHub 的全部功能，只追求让"记录创意、发布更新、管理项目"对普通人足够简单；免装 Git、中文界面与内容翻译都为这一个目标服务。对比基于各项目 2026 年 9 月公开资料整理。': 'EasyHub makes recording ideas, publishing updates, and managing projects simple for ordinary users. Its Git-free setup, bilingual interface, and content translation all serve that goal. This comparison is based on publicly available information from September 2026.',
    '下载发行版': 'Download EasyHub',
    'Windows 1.2.2 安装版与便携版': 'EasyHub 1.2.2 for Windows: installer and portable app',
    '安装版约 86.1 MiB，便携版约 85.8 MiB。两种版本都无需安装 Git。': 'The installer is about 86.1 MiB and the portable app about 85.8 MiB. Neither requires Git.',
    'Gitee 下载': 'Download from Gitee',
    'GitHub 下载': 'Download from GitHub',
    '下载安装版': 'Download installer',
    '下载便携版': 'Download portable app',
    '下载慢？切换下载来源': 'Slow download? Try another source',
    'Gitee 和 GitHub 均提供安装版与便携版，两个来源的文件一致。也可以查看': 'Both Gitee and GitHub offer the installer and portable app with identical files. You can also visit the',
    'Gitee 发布页': 'Gitee release page',
    'GitHub 发布页': 'GitHub release page',
    '和': ' and',
    '安装版': 'Installer',
    '便携版': 'Portable app',
    '适用于 Windows x64；尚未使用商业代码签名，首次运行可能提示“未知发布者”。': 'For Windows x64. The files are not commercially code signed, so Windows may show an “Unknown publisher” warning on first launch.',
    'macOS 1.2.2 桌面版': 'EasyHub 1.2.2 for macOS',
    '适用于 Apple 芯片 Mac，macOS 27 及以上。DMG 约 107.2 MiB，ZIP 约 98.2 MiB。': 'For Apple Silicon Macs running macOS 27 or later. The DMG is about 107.2 MiB and the ZIP about 98.2 MiB.',
    '下载 DMG': 'Download DMG',
    '下载 ZIP': 'Download ZIP',
    '打开 DMG，将 EasyHub 拖入 Applications。当前未通过 Apple 公证，首次打开请参考': 'Open the DMG and drag EasyHub into Applications. The app is not Apple notarized; for first launch, see the',
    '安装说明': 'installation guide',
    '。': '.',
    'Android 1.1.0 随身版': 'EasyHub 1.1.0 for Android',
    '在手机上查看项目、回复问题、下载发行版，也能审查合并请求。适用于 Android 7.0 及以上；本地文件发布在桌面版完成。': 'Browse projects, reply to issues, download releases, and review pull requests on your phone. Requires Android 7.0 or later; local file publishing is available on desktop.',
    '了解 Android 版': 'Explore Android app',
    '下载精简安装包': 'Download arm64 APK',
    '下载通用安装包': 'Download universal APK',
    '精简安装包约 26.2 MiB，适合大多数较新的手机；通用安装包约 44.5 MiB，支持 ARM32、ARM64、x86 和 x86_64。': 'The arm64 APK is about 26.2 MiB and suits most newer phones. The universal APK is about 44.5 MiB and supports ARM32, ARM64, x86, and x86_64.',
    '让 GitHub 简单到每个人都会用': 'Make GitHub simple for everyone',
    'EasyHub 是面向新手的开源 GitHub 客户端，提供 Windows、macOS 与 Android 版本，当前源代码采用 Apache-2.0 协议。通过 GitHub 授权登录，凭证保存在设备的安全存储中，无自有服务器。': 'EasyHub is an open source GitHub app for beginners on Windows, macOS and Android. The current source code is licensed under Apache-2.0. Sign in through GitHub; credentials stay in secure device storage, with no EasyHub server.',
    '© 2026 EasyHub · Windows / macOS 1.2.2 · Android 1.1.0 · 本页对比信息基于各项目 2026 年 9 月公开资料整理': '© 2026 EasyHub · Windows / macOS 1.2.2 · Android 1.1.0 · Comparison based on public project information from September 2026',
    'Gitee 仓库': 'Gitee repository',
    'GitHub 仓库': 'GitHub repository',
}

ATTRIBUTES = {
    'EasyHub - 简单易用的 GitHub 客户端，支持 Windows、macOS 与 Android': 'EasyHub - A simpler GitHub app for Windows, macOS and Android',
    'EasyHub 是面向新手的开源 GitHub 客户端。Windows / macOS 上免装 Git 发布作品，项目介绍可边写边看；Android 上查看项目、回复问题和审查合并请求。': 'EasyHub is an open source GitHub app for beginners. Publish on Windows or macOS without installing Git and preview project introductions as you write; browse projects and review pull requests on Android.',
    '免装 Git，一句话发布源码。Windows 项目介绍支持编辑、预览与边写边看，图片、表格和折叠内容都能预览，确认后再发布。': 'Publish code without installing Git. On Windows, use Edit, Preview, or Live Preview for project introductions, including images, tables, and expandable sections. Publish when ready.',
    'EasyHub：让 GitHub 简单到每个人都会用': 'EasyHub: Make GitHub simple for everyone',
    '免装 Git 管理项目和问题。Windows 项目介绍可以边写边看，保存后再发布；Android 随时查看项目与合并请求。': 'Manage GitHub projects and issues without installing Git. Preview project introductions as you write on Windows, save, then publish. Browse projects and pull requests on Android.',
    'EasyHub 图标': 'EasyHub icon',
    'EasyHub 盆栽': 'EasyHub potted plant',
    'EasyHub 热门手绘界面示意': 'Illustration of EasyHub Trending',
    'EasyHub 合并请求审查界面示意': 'Illustration of EasyHub Pull Request Reviews',
    '打开菜单': 'Open menu',
    '切换到浅色模式': 'Switch to light mode',
    '语言 / Language': 'Language',
    '查看 Gitee 仓库': 'View Gitee repository',
    '查看 GitHub 仓库': 'View GitHub repository',
}


def has_han(value: str) -> bool:
    return any('\u4e00' <= char <= '\u9fff' for char in value)


def translate_text(match: re.Match[str]) -> str:
    value = match.group(1)
    stripped = value.strip()
    if not has_han(stripped):
        return match.group(0)
    if stripped not in TEXT:
        raise ValueError(f'Missing English translation for: {stripped}')
    return '>' + value.replace(stripped, TEXT[stripped], 1) + '<'


def translate_attribute(match: re.Match[str]) -> str:
    name, value = match.groups()
    if not has_han(value):
        return match.group(0)
    if value not in ATTRIBUTES:
        raise ValueError(f'Missing English attribute translation: {name}={value}')
    return f'{name}="{ATTRIBUTES[value]}"'


def build() -> None:
    source = SOURCE.read_text(encoding='utf-8')
    head, body = source.split('<body id="top">', 1)
    visible, scripts = body.split('<noscript>', 1)
    visible = re.sub(r'>([^<>]+)<', translate_text, visible)
    result = head + '<body id="top">' + visible + '<noscript>' + scripts
    result = re.sub(r'([\w:-]+)="([^"\n]*)"', translate_attribute, result)
    result = result.replace('</a>\u3001<a ', '</a> or <a ')
    result = result.replace('GitHub release page</a>。</p>', 'GitHub release page</a>.</p>')

    result = result.replace('<html lang="zh-CN">', '<html lang="en">', 1)
    result = result.replace('<title>EasyHub - 简单易用的 GitHub 客户端 | Windows、macOS 与 Android</title>',
                            '<title>EasyHub - A simpler GitHub app for Windows, macOS and Android</title>', 1)
    result = result.replace('<meta property="og:locale" content="zh_CN">',
                            '<meta property="og:locale" content="en_US">', 1)
    result = result.replace('<link rel="canonical" href="https://fufu-flash.github.io/easyhub-website/">',
                            '<link rel="canonical" href="https://fufu-flash.github.io/easyhub-website/en.html">', 1)
    result = result.replace('<meta property="og:url" content="https://fufu-flash.github.io/easyhub-website/">',
                            '<meta property="og:url" content="https://fufu-flash.github.io/easyhub-website/en.html">', 1)
    result = result.replace('"url": "https://fufu-flash.github.io/easyhub-website/",',
                            '"url": "https://fufu-flash.github.io/easyhub-website/en.html",', 1)
    result = result.replace('"description": "面向新手的开源 GitHub 客户端。在 Windows 上发布作品，编辑项目介绍时可边写边看，也能用 AI 辅助审查代码与程序文件。",',
                            '"description": "An open source GitHub app for beginners. Publish on Windows, preview project introductions as you write, and use AI to review code and program files.",', 1)
    result = result.replace('"url": "https://fufu-flash.github.io/easyhub-website/android.html",',
                            '"url": "https://fufu-flash.github.io/easyhub-website/android-en.html",', 1)
    result = result.replace('"description": "在 Android 上查看 GitHub 项目、回复问题、下载发行版和审查合并请求。",',
                            '"description": "Browse GitHub projects, reply to issues, download releases, and review pull requests on Android.",', 1)
    result = result.replace('<a href="./" data-lang="zh" lang="zh-CN" aria-current="page">',
                            '<a href="./" data-lang="zh" lang="zh-CN">', 1)
    result = result.replace('<a href="en.html" data-lang="en" lang="en">',
                            '<a href="en.html" data-lang="en" lang="en" aria-current="page">', 1)
    result = result.replace('href="android.html"', 'href="android-en.html"')

    result = result.replace('"description": "Apple 芯片 Mac 上的开源 GitHub 客户端，用于创作、发布和管理项目。",',
                            '"description": "An open source GitHub app for creating, publishing and managing projects on Apple Silicon Macs.",', 1)
    result = result.replace('"url": "https://fufu-flash.github.io/easyhub-website/#download",',
                            '"url": "https://fufu-flash.github.io/easyhub-website/en.html#download",', 1)
    result = result.replace('https://github.com/FuFu-Flash/EasyHub#macos-%E5%BF%85%E7%9C%8B',
                            'https://github.com/FuFu-Flash/EasyHub/blob/main/README.en.md#macos-must-read', 1)

    # Text in CSS/HTML comments and the shared script can stay in Chinese.
    head, body = result.split('<body id="top">', 1)
    visible, _ = body.split('<noscript>', 1)
    visible = re.sub(r'<div class="language-switch".*?</div>', '', visible, flags=re.S)
    visible = re.sub(r'<!--.*?-->', '', visible, flags=re.S)
    visible = re.sub(r'<[^>]+>', '', visible)
    if has_han(unescape(visible)):
        raise ValueError('Visible Chinese text remains on the English page')
    OUTPUT.write_bytes(result.encode('utf-8'))


if __name__ == '__main__':
    build()
