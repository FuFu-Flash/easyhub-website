"""Build the English Android landing page from the Chinese page."""

from html import unescape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / 'android.html'
OUTPUT = ROOT / 'android-en.html'

TEXT = {
    'EasyHub Android 1.1.0 | 随时查看 GitHub 项目': 'EasyHub Android 1.1.0 | Your GitHub projects on the go',
    '首页': 'Home', '功能': 'Features', '下载 Android 版': 'Download Android',
    '中文': '中文', '你的项目，': 'Your projects,', '随时在手边。': 'wherever you are.',
    '在电脑上发布，在手机上接着看。浏览项目、回复问题、下载发行版，也能查看和审查合并请求。': 'Publish on your computer and stay connected on your phone. Browse projects, reply to issues, download releases, and review pull requests.',
    '了解桌面版': 'Explore desktop app',
    '免费开源 · Android 7.0 及以上 · 使用 GitHub 登录': 'Free and open source · Android 7.0+ · Sign in with GitHub',
    '项目已更新': 'Project updated', '刚刚': 'Just now', '你': 'Y',
    '你的创作空间': 'Your creative space',
    '今天也来做点有趣的事情。': 'Let’s make something fun today.',
    '＋ 新建项目': '＋ New project', '接着创作': 'Keep creating',
    '你的项目都已保存。': 'Your projects are saved.',
    '打开项目，继续创作。': 'Open a project and keep creating.',
    '查看项目 →': 'View projects →', '一个 Windows 小工具': 'A handy Windows tool',
    '● 已保存': '● Saved',
    '我的网站': 'My website', '我的个人主页': 'My personal page',
    '早上好 👋': 'Good morning 👋', '你的项目都在这里。': 'Your projects are here.',
    '我的项目': 'My projects', '查看全部 ›': 'View all ›',
    '1 个待处理的问题': '1 open issue', '刚刚更新': 'Updated just now',
    '近期动态': 'Recent activity', '修复窗口缩放问题': 'Fixed window resizing',
    'Minecraft Mod · 今天': 'Minecraft Mod · Today', '项目': 'Projects',
    '问题': 'Issues', '设置': 'Settings', '随时查看': 'Keep up anywhere',
    '与 Windows 同步': 'In sync with Windows', '带着项目走': 'Take your projects along',
    '出门后，也能跟上项目的每一步。': 'Keep up with every step of your project.',
    'EasyHub Android 直接读取 GitHub 内容。电脑发布更新后，手机打开项目就能看到。': 'EasyHub Android reads directly from GitHub. Publish on your computer, then open the project on your phone to see the update.',
    '01 / 浏览': '01 / Browse', '02 / 交流': '02 / Discuss',
    '03 / 发现': '03 / Discover', '04 / 合并请求审查': '04 / Pull Request Reviews',
    '项目和版本，都在手机里。': 'Projects and releases, right in your pocket.',
    '查看自己的项目与公开项目，阅读介绍、历史版本和发行说明，再选择要下载的文件。': 'Browse your projects and public projects, read descriptions and history, then choose the release files you want.',
    '历史版本 · 问题 · 下载': 'History · Issues · Downloads',
    '看到问题，直接回复。': 'See an issue? Reply right away.',
    '创建、回复、关闭或重新打开问题；在手机上也能继续和项目使用者交流。': 'Create, reply to, close, or reopen issues. Keep the conversation going from your phone.',
    '找到值得关注的作品。': 'Find projects worth following.',
    '搜索公开项目和用户，浏览 EasyHub 热门。热门排序由 EasyHub 提供，并非 GitHub 官方 Trending。': 'Search public projects and people, or browse EasyHub Trending. This ranking is made by EasyHub, not GitHub Trending.',
    '合并请求，先看清楚再决定。': 'Understand pull requests before deciding.',
    '在“合并请求审查”中查看修改、发表意见。按需使用自己配置的 AI 服务整理风险与建议；批准或拒绝始终由你决定。': 'In Pull Request Reviews, inspect changes and leave comments. If you choose, use your own AI provider to summarize risks and suggestions. You always decide whether to approve or reject.',
    '查看修改': 'Inspect changes', 'AI 辅助审查': 'AI assisted review',
    '由你决定': 'Your decision', '各有所长': 'Each platform has its place',
    '桌面创作，Android 随行。': 'Create on desktop. Keep up on Android.',
    '选择本地文件夹、检测文件变化、发布源码和上传新版本，在桌面版（Windows / macOS）完成。两端使用同一个 GitHub 账号，项目、问题与版本通过 GitHub 保持一致。': 'Choose local folders, detect file changes, publish code, and upload new releases on Windows or macOS. Sign in to the same GitHub account on both devices to see the same projects, issues, and releases.',
    '查看桌面版': 'See desktop app', '开始使用': 'Get started',
    '选择适合手机的安装包。': 'Choose the right APK for your phone.',
    '大多数较新的 Android 手机选择精简安装包；如果无法安装，再试通用安装包。': 'Choose the smaller APK for most newer Android phones. If it does not install, try the universal APK.',
    '推荐': 'Recommended', '兼容选择': 'Compatibility option',
    '精简安装包': 'Smaller APK', '通用安装包': 'Universal APK',
    '适合大多数较新的 Android 手机，约 26.2 MiB。': 'For most newer Android phones, about 26.2 MiB.',
    '精简版无法安装时使用，约 44.5 MiB，支持 ARM32、ARM64、x86 和 x86_64。': 'Try this if the smaller APK does not install, about 44.5 MiB. Supports ARM32, ARM64, x86, and x86_64.',
    '从 Gitee 下载': 'Download from Gitee', '从 GitHub 下载': 'Download from GitHub',
    '下载 APK 后，按 Android 系统提示允许安装。iOS 版尚未推出。': 'After downloading the APK, follow Android prompts to allow installation. An iOS app is not available yet.',
    '查看完整发行版': 'View the full release',
    '当前源代码：Apache-2.0 · Android v1.1.0': 'Current source: Apache-2.0 · Android v1.1.0',
    '网站首页': 'Website home', 'Gitee 仓库': 'Gitee repository',
    'GitHub 仓库': 'GitHub repository',
}

ATTRIBUTES = {
    'EasyHub Android 版让你在手机上查看 GitHub 项目、回复问题、下载发行版和审查合并请求。提供精简与通用安装包。': 'EasyHub for Android helps you browse GitHub projects, reply to issues, download releases, and review pull requests. Choose from two APKs.',
    'EasyHub Android | 你的项目，随时在手边': 'EasyHub Android | Your projects, wherever you are',
    '在手机上查看项目、回复问题、下载发行版和审查合并请求。': 'Browse projects, reply to issues, download releases, and review pull requests on your phone.',
    '主导航': 'Main navigation', '切换到浅色模式': 'Switch to light mode',
    '语言 / Language': 'Language',
    'EasyHub Android 项目首页手绘示意': 'Hand drawn preview of the EasyHub Android home screen',
    '安卓应用截图预留位置': 'Reserved space for an Android app screenshot',
    '根据 EasyHub Android 首页绘制的界面预览': 'Illustrated preview based on the EasyHub Android home screen',
}


def has_han(value: str) -> bool:
    return any('\u4e00' <= char <= '\u9fff' for char in value)


def replace_text(match: re.Match[str]) -> str:
    value = match.group(1)
    stripped = value.strip()
    if not has_han(stripped):
        return match.group(0)
    if stripped not in TEXT:
        raise ValueError(f'Missing Android translation: {stripped}')
    return '>' + value.replace(stripped, TEXT[stripped], 1) + '<'


def replace_attribute(match: re.Match[str]) -> str:
    name, value = match.groups()
    if not has_han(value):
        return match.group(0)
    if value not in ATTRIBUTES:
        raise ValueError(f'Missing Android attribute: {name}={value}')
    return f'{name}="{ATTRIBUTES[value]}"'


def build() -> None:
    source = SOURCE.read_text(encoding='utf-8')
    result = re.sub(r'>([^<>]+)<', replace_text, source)
    result = re.sub(r'([\w:-]+)="([^"\n]*)"', replace_attribute, result)
    result = result.replace('<html lang="zh-CN">', '<html lang="en">', 1)
    result = result.replace("      if(language==='en'||(!language&&!browser.toLowerCase().startsWith('zh')))location.replace(new URL('android-en.html'+location.search+location.hash,location.href));",
                            "      // Direct navigation to the English page keeps the explicit language choice.", 1)
    result = result.replace('href="https://fufu-flash.github.io/easyhub-website/android.html"',
                            'href="https://fufu-flash.github.io/easyhub-website/android-en.html"', 1)
    result = result.replace('content="https://fufu-flash.github.io/easyhub-website/android.html"',
                            'content="https://fufu-flash.github.io/easyhub-website/android-en.html"', 1)
    result = result.replace('"url":"https://fufu-flash.github.io/easyhub-website/android.html"',
                            '"url":"https://fufu-flash.github.io/easyhub-website/android-en.html"', 1)
    result = result.replace('<a href="android.html" data-lang="zh" aria-current="page">',
                            '<a href="android.html" data-lang="zh">', 1)
    result = result.replace('<a href="android-en.html" data-lang="en">',
                            '<a href="android-en.html" data-lang="en" aria-current="page">', 1)
    visible = re.sub(r'<script.*?</script>', '', result, flags=re.S)
    visible = re.sub(r'<[^>]+>', '', visible)
    if has_han(unescape(visible.replace('中文', ''))):
        raise ValueError('Chinese text remains on Android English page')
    OUTPUT.write_text(result, encoding='utf-8', newline='\n')


if __name__ == '__main__':
    build()
