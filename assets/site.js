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
  // 记住手动选择的语言，并保留当前所在的区块
  document.querySelectorAll('.lang a[data-lang]').forEach(function(link){
    link.addEventListener('click',function(){
      try{localStorage.setItem('easyhub-site-language',link.dataset.lang)}catch(e){}
      link.href=link.getAttribute('href').split('#')[0]+location.hash;
    });
  });
})();
