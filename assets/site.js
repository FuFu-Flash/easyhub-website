(function(){
  var root=document.documentElement;
  var english=root.lang==='en';
  var themeToggle=document.getElementById('themeToggle');
  function updateThemeButton(){
    var dark=root.dataset.theme==='dark';
    var label=english?(dark?'Switch to light mode':'Switch to dark mode'):(dark?'切换到浅色模式':'切换到深色模式');
    themeToggle.setAttribute('aria-label',label);
    themeToggle.setAttribute('title',label);
    themeToggle.setAttribute('aria-pressed',String(dark));
  }
  themeToggle.addEventListener('click',function(){
    var next=root.dataset.theme==='dark'?'light':'dark';
    root.dataset.theme=next;
    try{localStorage.setItem('easyhub-site-theme',next)}catch(e){}
    updateThemeButton();
  });
  if(window.matchMedia){
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change',function(event){
      var saved='';
      try{saved=localStorage.getItem('easyhub-site-theme')||''}catch(e){}
      if(saved!=='light'&&saved!=='dark'){root.dataset.theme=event.matches?'dark':'light';updateThemeButton()}
    });
  }
  updateThemeButton();
  // 页面滚动后顶栏加一层浅阴影
  var topbar=document.querySelector('.topbar');
  function updateTopbar(){topbar.classList.toggle('scrolled',window.scrollY>4)}
  window.addEventListener('scroll',updateTopbar,{passive:true});
  updateTopbar();
  // 滚动渐显：出现后移除标记，悬停动画恢复原来的快节奏；任何情况下都不留空白区块
  var reveals=document.querySelectorAll('.reveal');
  function finish(el){
    el.classList.add('in');
    el.addEventListener('transitionend',function done(event){
      if(event.target!==el||event.propertyName!=='opacity')return;
      el.classList.remove('reveal','in');
      el.removeEventListener('transitionend',done);
    });
  }
  if(!root.classList.contains('motion-ready')||!('IntersectionObserver' in window)){
    reveals.forEach(function(el){el.classList.remove('reveal')});
  }else{
    var observer=new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if(entry.isIntersecting){finish(entry.target);observer.unobserve(entry.target)}
      });
    },{threshold:.12,rootMargin:'0px 0px -40px 0px'});
    reveals.forEach(function(el){observer.observe(el)});
    window.addEventListener('load',function(){
      setTimeout(function(){document.querySelectorAll('.reveal:not(.in)').forEach(finish)},3000);
    });
  }
  // 记住手动选择的语言，并保留当前所在的区块
  document.querySelectorAll('.lang a[data-lang]').forEach(function(link){
    link.addEventListener('click',function(){
      try{localStorage.setItem('easyhub-site-language',link.dataset.lang)}catch(e){}
      link.href=link.getAttribute('href').split('#')[0]+location.hash;
    });
  });
})();
