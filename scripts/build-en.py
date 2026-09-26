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
    '开源 · GPL-3.0 · Windows 桌面客户端 v1.2.0': 'Open source · GPL-3.0 · Windows desktop app v1.2.0',
    '让 GitHub': 'Make GitHub',
    '简单到每个人都会用': 'simple for everyone',
    '不用学命令行，也不用安装 Git。找回电脑上已有的项目，或选择文件夹开始创作；写一句更新说明就能发布源码。收到代码改进时，还能用 AI 辅助审查，由你决定是否采纳。': 'No command line or Git installation required. Find projects already on your computer or choose a folder to start creating. Write a short update to publish your code. When someone proposes a change, AI can help you review it while you make the final decision.',
    '下载与运行': 'Download',
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
    '使用 GitHub 登录后管理项目、发布源码与新版本、回复问题，还能用 AI 辅助审查别人提交的代码改进。访问令牌保存在 Windows 凭证管理器，无需 EasyHub 账号或自有服务器。': 'Sign in with GitHub to manage projects, publish code and releases, reply to issues, and use AI to review proposed changes. Your access token stays in Windows Credential Manager; EasyHub needs no separate account or server.',
    'v1.2.0 新增 · AI 辅助审查': 'New in v1.2.0 · AI assisted review',
    '收到代码改进，先看清楚再决定': 'Review proposed changes before you decide',
    '先查看对方修改的文件，再让 AI 整理可能的问题和修改建议。每次审查前都会显示要发送的内容和所选服务，得到你的确认才开始；批准或拒绝始终由你决定。': 'Inspect the changed files first, then let AI summarize potential issues and suggestions. EasyHub shows what will be sent and to which service before every review. Nothing is sent until you confirm, and you decide whether to approve or reject.',
    '自带 API Key': 'Bring your own API key',
    '确认后才发送': 'Sent only after confirmation',
    '不会自动合入': 'Never merges automatically',
    '只分析可读取的文字修改，不运行程序或测试；结果仅供参考，服务商可能收费。': 'Only readable text changes are reviewed; no code or tests are run. Results are advisory, and your AI provider may charge for usage.',
    'AI 审查建议': 'AI review suggestions',
    '由你决定': 'You decide',
    '修改文件': 'Changed files',
    '可能需要检查设置保存时机': 'Check when settings are saved',
    '关闭窗口后重新打开，确认设置仍然保留。': 'Close and reopen the window to confirm that settings are retained.',
    '建议仅供参考': 'Suggestions only',
    '拒绝': 'Reject',
    '批准': 'Approve',
    '使用 GitHub 安全登录': 'Secure GitHub sign-in',
    '通过 GitHub 设备授权登录，无需另建账号。访问令牌由 Windows 凭证管理器保存；项目资料从 GitHub 获取，不需要 EasyHub 云端服务。': 'Sign in through GitHub device authorization. There is no separate EasyHub account. Windows Credential Manager stores your token, and project data comes directly from GitHub.',
    '本地文件夹发布源码': 'Publish from a local folder',
    '选择文件夹即可识别项目；也能指定位置，找回已连接到自己 GitHub 项目的文件夹。后台扫描新增、修改、删除和重命名的文件，遵守 .gitignore、避开依赖目录；无需安装 Git。': 'Choose a folder to make it a project, or search a location for folders already connected to your GitHub projects. Background scanning detects added, changed, deleted, and renamed files while respecting .gitignore and skipping dependency folders. No Git installation is required.',
    '冲突安全处理': 'Safe conflict handling',
    '发布前先检查云端：可安全衔接的更新自动先获取；双方改动同一文件时，双版本预览、逐个选择保留版本。复杂历史会阻止自动发布，绝不强制覆盖。': 'EasyHub checks GitHub before publishing. Compatible updates are fetched first; if the same file changed in two places, you can compare both versions and choose what to keep. Complex cases stop the publish instead of overwriting files.',
    '问题与改进请求': 'Issues and contributions',
    '创建和回复问题，关闭或重新打开；问题列表按项目分组并可继续加载。项目页还能查看改进请求，也能为其他项目准备并提交代码改进。': 'Create and reply to issues, close or reopen them, and load more results in project groups. View pull requests on project pages, and prepare code improvements for other projects to review.',
    '发布新版本 Release': 'Publish downloadable releases',
    '正式版、Alpha、Beta 三种类型，自动建议并续号版本名；可插入链接与图片、选择多个下载文件，按 GitHub 公开限制校验（单文件小于 2 GiB、每版最多 1000 个、不可同名），随后真实创建 Release、逐个上传附件，已完成端到端验收。': 'Choose a stable, Alpha, or Beta release and get a suggested version number. Add links, images, and multiple downloads; EasyHub checks GitHub limits before creating the release and uploading each file.',
    '公开内容翻译': 'Translate public content',
    '一键统一翻译项目简介、README、问题与 Release 描述；README 按段落随滚动逐步翻译。私有项目不发送给第三方，项目名、版本号、文件名以占位符保护，译文本地缓存。': 'Translate public project summaries, READMEs, issues, and release notes with one switch. README paragraphs translate as you scroll. Private projects are not sent to the translation provider, and names, versions, and filenames stay intact.',
    '发现好项目': 'Discover projects',
    '今天有什么值得关注？打开 EasyHub 热门看看': 'Find something worth exploring with EasyHub Trending',
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
    '下载已发布版本，或从源码运行': 'Download EasyHub or run it from source',
    'Windows 1.2.0 安装版与便携版': 'EasyHub 1.2.0 for Windows: installer and portable app',
    '选择适合自己的版本和下载来源。两种版本都无需安装 Git：': 'Choose the edition and download source that suit you. Neither requires Git:',
    'Gitee 下载': 'Download from Gitee',
    'GitHub 下载': 'Download from GitHub',
    '下载安装版': 'Download installer',
    '下载便携版': 'Download portable app',
    '下载慢或失败？查看说明与文件校验': 'Slow or failed download? Check the sources and file hashes',
    '可以切换 Gitee 或 GitHub 下载，也可以在': 'Try Gitee or GitHub, or choose a file on the',
    'Gitee 发布页': 'Gitee release page',
    'GitHub 发布页': 'GitHub release page',
    '选择文件。': '.',
    '如果从其他地方取得安装包，请核对 SHA-256：': 'If you got a file elsewhere, verify its SHA-256 hash:',
    '安装版': 'Installer',
    '便携版': 'Portable app',
    '仅提供 Windows x64；尚未使用商业代码签名，首次运行可能提示“未知发布者”。': 'Windows x64 only. The files are not commercially code signed, so Windows may show an “Unknown publisher” warning on first launch.',
    '从源码运行': 'Run from source',
    '环境要求：': 'Requirements:',
    'Windows 系统': 'Windows',
    'Node.js 22 或更高': 'Node.js 22 or later',
    'pnpm 11 或更高': 'pnpm 11 or later',
    '# 安装依赖并启动': '# Install dependencies and start',
    '检查与构建': 'Check and build',
    '项目提供 TypeScript 检查、Lint、单元测试与界面点击测试，交付前可完整检查：': 'The project includes TypeScript checks, linting, unit tests, and UI click tests. Run them before a release:',
    '界面冒烟测试运行 pnpm test:ui。': 'Run UI smoke checks with pnpm test:ui.',
    '当前版本': 'Current version',
    '· 功能范围与构建方式见项目说明': '· See the repository for features and build instructions',
    '让 GitHub 简单到每个人都会用': 'Make GitHub simple for everyone',
    'EasyHub 是面向新手的开源 GitHub Windows 桌面客户端，以 GPL-3.0-only 协议发布。通过 OAuth 设备授权直连 GitHub，访问令牌仅保存在 Windows 凭证管理器，无自有服务器。': 'EasyHub is an open source GitHub desktop app for Windows, designed for beginners and licensed under GPL-3.0-only. It signs in through GitHub device authorization, stores tokens in Windows Credential Manager, and needs no EasyHub server.',
    '© 2026 EasyHub · v1.2.0 · 本页对比信息基于各项目 2026 年 9 月公开资料整理': '© 2026 EasyHub · v1.2.0 · Comparison based on public project information from September 2026',
    'Gitee 仓库': 'Gitee repository',
    'GitHub 仓库': 'GitHub repository',
}

ATTRIBUTES = {
    'EasyHub - 简单易用的 GitHub Windows 客户端': 'EasyHub - A simpler GitHub app for Windows',
    'EasyHub 是面向新手的开源 GitHub Windows 客户端。免装 Git，管理项目、发布源码和新版本，并用 AI 辅助审查代码改进；最终操作由用户决定。': 'EasyHub is an open source GitHub app for Windows. Manage projects, publish code and releases without installing Git, and use AI to review proposed changes while you make the final decision.',
    '免装 Git，一句话发布源码；收到改进请求时，用 AI 整理可能的问题和建议，批准或拒绝由你决定。': 'Publish code without installing Git. Use AI to summarize potential issues in proposed changes, then decide whether to approve or reject.',
    'EasyHub：让 GitHub 简单到每个人都会用': 'EasyHub: Make GitHub simple for everyone',
    '免装 Git 管理项目和问题，AI 辅助审查代码改进；最后由你决定是否采纳。': 'Manage GitHub projects and issues without installing Git. AI helps review proposed changes; you make the final decision.',
    'EasyHub 图标': 'EasyHub icon',
    'EasyHub 盆栽': 'EasyHub potted plant',
    'EasyHub 热门手绘界面示意': 'Illustration of EasyHub Trending',
    'EasyHub AI 辅助审查界面示意': 'Illustration of EasyHub AI assisted review',
    '打开菜单': 'Open menu',
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

    result = result.replace('<html lang="zh-CN">', '<html lang="en">', 1)
    result = result.replace('<title>EasyHub - 简单易用的 GitHub Windows 客户端 | 免装 Git</title>',
                            '<title>EasyHub - A simpler GitHub app for Windows | No Git install</title>', 1)
    result = result.replace('<meta property="og:locale" content="zh_CN">',
                            '<meta property="og:locale" content="en_US">', 1)
    result = result.replace('<link rel="canonical" href="https://fufu-flash.github.io/easyhub-website/">',
                            '<link rel="canonical" href="https://fufu-flash.github.io/easyhub-website/en.html">', 1)
    result = result.replace('<meta property="og:url" content="https://fufu-flash.github.io/easyhub-website/">',
                            '<meta property="og:url" content="https://fufu-flash.github.io/easyhub-website/en.html">', 1)
    result = result.replace('"url": "https://fufu-flash.github.io/easyhub-website/",',
                            '"url": "https://fufu-flash.github.io/easyhub-website/en.html",', 1)
    result = result.replace('"description": "面向新手的开源 GitHub Windows 桌面客户端，可管理项目、发布源码和版本，并用 AI 辅助审查代码改进。",',
                            '"description": "An open source GitHub desktop app for Windows. Manage projects, publish code and releases, and use AI to review proposed changes.",', 1)
    result = result.replace('<a href="./" data-lang="zh" lang="zh-CN" aria-current="page">',
                            '<a href="./" data-lang="zh" lang="zh-CN">', 1)
    result = result.replace('<a href="en.html" data-lang="en" lang="en">',
                            '<a href="en.html" data-lang="en" lang="en" aria-current="page">', 1)

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
