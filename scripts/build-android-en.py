"""Build the English Android page (android-en.html) from the Chinese page (android.html)."""

from pathlib import Path
import re

root = Path(__file__).resolve().parent.parent
src = (root / 'android.html').read_text(encoding='utf-8')
R = [
('<html lang="zh-CN">', '<html lang="en">'),
("""  if(language==='en'||(!language&&!browser.toLowerCase().startsWith('zh'))){
    location.replace(new URL('android-en.html'+location.search+location.hash,location.href));
  }
""", ""),
('<title>EasyHub Android - 在手机上查看 GitHub 项目</title>', '<title>EasyHub Android - Your GitHub projects on your phone</title>'),
('content="EasyHub Android 版让你在手机上查看 GitHub 项目、回复问题、下载发行版和审查合并请求。适用于 Android 7.0 及以上，免费开源。"', 'content="EasyHub for Android lets you browse GitHub projects, reply to issues, download releases and review pull requests on your phone. Free and open source for Android 7.0 and later."'),
('<link rel="canonical" href="https://fufu-flash.github.io/easyhub-website/android.html">', '<link rel="canonical" href="https://fufu-flash.github.io/easyhub-website/android-en.html">'),
('content="zh_CN"', 'content="en_US"'),
('content="EasyHub Android - 你的项目，随时在手边"', 'content="EasyHub Android - Your projects, wherever you are"'),
('content="在手机上查看项目、回复问题、下载发行版和审查合并请求。"', 'content="Browse projects, reply to issues, download releases and review pull requests on your phone."'),
('<meta property="og:url" content="https://fufu-flash.github.io/easyhub-website/android.html">', '<meta property="og:url" content="https://fufu-flash.github.io/easyhub-website/android-en.html">'),
('"url": "https://fufu-flash.github.io/easyhub-website/android.html"', '"url": "https://fufu-flash.github.io/easyhub-website/android-en.html"'),
('"在 Android 上查看 GitHub 项目、回复问题、下载发行版和审查合并请求。"', '"Browse GitHub projects, reply to issues, download releases and review pull requests on Android."'),
('"downloadUrl": "https://gitee.com/HUAJILA/easy-hub/releases/download/android-v1.2.0/', '"downloadUrl": "https://github.com/FuFu-Flash/EasyHub/releases/download/android-v1.2.0/'),
('跳到正文', 'Skip to content'),
('aria-label="页面导航"', 'aria-label="Page sections"'),
('>功能</a>', '>Features</a>'), ('>下载</a>', '>Download</a>'),
('<a href="./?platform=windows">桌面版</a>', '<a href="en.html?platform=windows">Desktop</a>'),
('<a class="brand" href="./?platform=windows">', '<a class="brand" href="en.html?platform=windows">'),
('aria-label="在 GitHub 查看源码" title="在 GitHub 查看源码"', 'aria-label="View source on GitHub" title="View source on GitHub"'),
('aria-label="切换到深色模式" title="切换到深色模式"', 'aria-label="Switch to dark mode" title="Switch to dark mode"'),
('<a href="android.html" data-lang="zh" lang="zh-CN" aria-current="page">中文</a>', '<a href="android.html" data-lang="zh" lang="zh-CN">中文</a>'),
('<a href="android-en.html" data-lang="en" lang="en">EN</a>', '<a href="android-en.html" data-lang="en" lang="en" aria-current="page">EN</a>'),
('<h1>你的项目，随时在手边</h1>', '<h1>Your projects, wherever you are</h1>'),
('在电脑上发布，在手机上接着看。浏览项目、回复问题、下载发行版，也能审查合并请求。', 'Publish on your computer, keep up on your phone. Browse projects, reply to issues, download releases and review pull requests.'),
('下载 Android 版\n        </a>', 'Download for Android\n        </a>'),
('<a class="btn btn-secondary btn-lg" href="./?platform=windows">了解桌面版</a>', '<a class="btn btn-secondary btn-lg" href="en.html?platform=windows">Desktop app</a>'),
('<span><i></i>Android 7.0 及以上</span>', '<span><i></i>Android 7.0 or later</span>'),
('<span>用 GitHub 登录</span>', '<span>Sign in with GitHub</span>'),
('<span>Apache-2.0 开源</span>', '<span>Apache-2.0 open source</span>'),
('<strong>首页</strong>', '<strong>Home</strong>'),
('等你处理 <span>2</span>', 'Needs your attention <span>2</span>'),
('<small>1 个待处理的问题 · 1 个待审查的合并请求</small>', '<small>1 open issue · 1 pull request to review</small>'),
('<span class="phone-btn">去审查</span>', '<span class="phone-btn">Review</span>'),
('还有 1 个项目', '1 more project'),
('<p class="phone-label">我的项目</p><span>全部 4 个 ›</span>', '<p class="phone-label">My projects</p><span>All 4 ›</span>'),
('已保存 · 刚刚', 'Saved · just now'), ('已保存 · 2 小时前', 'Saved · 2 hours ago'), ('已保存 · 3 天前', 'Saved · 3 days ago'),
('<strong>我的网站</strong>', '<strong>My website</strong>'),
('<strong>1.2.0 换了新的签名，从旧版升级要先卸载</strong>', '<strong>1.2.0 has a new signing key. Uninstall the old version before upgrading</strong>'),
('1.1.0 及更早的安装包用的是公开的调试签名，别人也能做出同签名的假安装包。从 1.2.0 起改用 EasyHub 自己的签名。卸载旧版后需要重新登录 GitHub，你在 GitHub 上的项目不受影响。', '1.1.0 and earlier were signed with a public debug key, so anyone could make a look-alike package. From 1.2.0 on, EasyHub uses its own key. After uninstalling you need to sign in to GitHub again; your projects on GitHub are not affected.'),
('<p class="section-label">功能</p>', '<p class="section-label">Features</p>'),
('出门在外，也能跟上项目', 'Keep up with your projects on the go'),
('手机直接读取 GitHub 上的内容。电脑上发布了更新，手机打开项目就能看到。', 'The app reads straight from GitHub. Publish an update on your computer and it shows up when you open the project on your phone.'),
('<h3>首页就是待办</h3>', '<h3>Your home page is your to-do list</h3>'),
('“等你处理”把同一个项目的问题和待审查的合并请求合成一行，其余的折叠起来，打开就知道先做什么。', 'Needs your attention puts a project\'s open issues and pull requests to review on one row and folds away the rest, so you know what to do first.'),
('<h3>看到问题，直接回复</h3>', '<h3>Reply to issues right away</h3>'),
('提出、回复、关闭或重新打开问题，在手机上也能和使用你项目的人继续交流。', 'Open, reply to, close or reopen issues, and keep talking with the people who use your project.'),
('<h3>合并请求，先看清楚</h3>', '<h3>See pull requests clearly</h3>'),
('查看改了哪些文件。批准合并前会显示改动文件数和检查结果，检查没通过会提醒你。', 'See which files changed. Before you approve and merge, you see the number of changed files and the check results, with a warning if checks failed.'),
('<h3>项目和版本都在手里</h3>', '<h3>Projects and releases in your pocket</h3>'),
('阅读项目介绍、修改记录和发行说明，选好文件直接下载到手机，能看到进度，也能取消。', 'Read READMEs, history and release notes, then download files straight to your phone with progress and a cancel button.'),
('<h3>发现好项目</h3>', '<h3>Discover projects</h3>'),
('搜索公开项目和用户，看看 EasyHub 热门。外文介绍和问题可以一键翻译。', 'Search public projects and people, and browse EasyHub Trending. Translate READMEs and issues with one tap.'),
('<h3>深色模式</h3>', '<h3>Dark mode</h3>'),
('在设置的“外观”里选跟随系统、浅色或深色，配色和桌面版一致，晚上看也不刺眼。', 'Choose Follow system, Light or Dark under Settings → Appearance. The colors match the desktop app and are easy on the eyes at night.'),
('<p class="section-label">和桌面版的分工</p>', '<p class="section-label">Phone and desktop</p>'),
('手机随身看，电脑来发布', 'Check on your phone, publish on your computer'),
('两边登录同一个 GitHub 账号，项目、问题和版本通过 GitHub 保持一致。', 'Sign in with the same GitHub account on both. Projects, issues and releases stay in sync through GitHub.'),
('<span class="split-dot ok"></span>手机上可以', '<span class="split-dot ok"></span>On your phone'),
('<li>查看自己的项目和公开项目</li>', '<li>Browse your projects and public projects</li>'),
('<li>提出和回复问题</li>', '<li>Open and reply to issues</li>'),
('<li>审查、合并或关闭合并请求</li>', '<li>Review, merge or close pull requests</li>'),
('<li>新建项目、下载发行版</li>', '<li>Create projects and download releases</li>'),
('<span class="split-dot"></span>需要用桌面版', '<span class="split-dot"></span>Needs the desktop app'),
('<li>管理电脑上的项目文件夹</li>', '<li>Manage project folders on your computer</li>'),
('<li>发布源码</li>', '<li>Publish code</li>'),
('<li>发布或编辑新版本</li>', '<li>Publish or edit releases</li>'),
('<a class="split-link" href="./?platform=windows#download">下载桌面版 →</a>', '<a class="split-link" href="en.html?platform=windows#download">Get the desktop app →</a>'),
('<p class="section-label">下载</p>', '<p class="section-label">Download</p>'),
('<h2 class="section-title">下载 Android 版</h2>', '<h2 class="section-title">Download for Android</h2>'),
('下载后按系统提示允许安装。从 1.1.0 或更早版本升级，请先卸载旧版。', 'After downloading, allow the install when Android asks. Upgrading from 1.1.0 or earlier? Uninstall the old version first.'),
('<span>安装包</span><span>适用于</span>', '<span>Package</span><span>Requirements</span>'),
('<small>ARM64 安装包 · 约 26 MB</small>', '<small>ARM64 package · about 26 MB</small>'),
('<b>Android 7.0 及以上</b><br>适合大多数较新的手机', '<b>Android 7.0 or later</b><br>For most newer phones'),
('这一版暂时没有通用安装包，ARM32 和 x86 设备请等后续版本。旧的 1.1.0 通用包用的是公开调试签名，不再提供。', 'There is no universal package for this version yet; ARM32 and x86 devices need to wait for a later release. The old 1.1.0 universal package used the public debug key and is no longer offered.'),
('<summary>核对安装包是否来自 EasyHub</summary>', '<summary>Check that the package comes from EasyHub</summary>'),
('只从本页或发行版页面下载。安装包和签名证书的 SHA-256 应与下面一致：', 'Download only from this page or the release page. The SHA-256 of the package and signing certificate should match:'),
('<dt>安装包</dt>', '<dt>Package</dt>'), ('<dt>签名证书</dt>', '<dt>Certificate</dt>'),
('<li>iOS 版还没有推出。</li>', '<li>There is no iOS app yet.</li>'),
('完整更新说明在 <a href="https://gitee.com/HUAJILA/easy-hub/releases/tag/android-v1.2.0" target="_blank" rel="noopener noreferrer">Gitee 发布页</a> 和 <a href="https://github.com/FuFu-Flash/EasyHub/releases/tag/android-v1.2.0" target="_blank" rel="noopener noreferrer">GitHub 发布页</a>。', 'Full release notes are on the <a href="https://github.com/FuFu-Flash/EasyHub/releases/tag/android-v1.2.0" target="_blank" rel="noopener noreferrer">GitHub release page</a> and the <a href="https://gitee.com/HUAJILA/easy-hub/releases/tag/android-v1.2.0" target="_blank" rel="noopener noreferrer">Gitee release page</a>.'),
('<span>Apache-2.0 开源 · 使用 GitHub 账号登录，没有自己的服务器</span>', '<span>Apache-2.0 open source · Signs in with your GitHub account, no EasyHub servers</span>'),
('aria-label="外部链接"', 'aria-label="Links"'), ('>反馈问题</a>', '>Report an issue</a>'),
]
for a, b in R:
    if a not in src:
        raise SystemExit(f'Missing source text: {a[:60]}')
    src = src.replace(a, b)
# English visitors get GitHub first; the Chinese page leads with Gitee
apk = 'android-v1.2.0/EasyHub-Android-1.2.0-arm64.apk'
pair = (f'<a class="btn btn-primary btn-sm" href="https://gitee.com/HUAJILA/easy-hub/releases/download/{apk}">从 Gitee 下载</a>\n'
        f'          <a class="btn btn-secondary btn-sm" href="https://github.com/FuFu-Flash/EasyHub/releases/download/{apk}">从 GitHub 下载</a>')
if pair not in src:
    raise SystemExit('Download buttons changed')
src = src.replace(pair, f'<a class="btn btn-primary btn-sm" href="https://github.com/FuFu-Flash/EasyHub/releases/download/{apk}">Download from GitHub</a>\n'
                        f'          <a class="btn btn-secondary btn-sm" href="https://gitee.com/HUAJILA/easy-hub/releases/download/{apk}">From Gitee</a>')
(root / 'android-en.html').write_text(src, encoding='utf-8', newline='')
leftover = [m for m in re.findall(r'[一-鿿][^<>"]*', src) if m not in ('中文', '语言 / Language')]
if leftover:
    raise SystemExit(f'Untranslated text: {leftover}')
