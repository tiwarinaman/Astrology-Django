CKEDITOR.replace('user_info');
CKEDITOR.plugins.addExternal('abbr', '/myplugins/abbr/', 'plugin.js');


CKEDITOR.replace('user_info', {
    extraPlugins: 'abbr'
});
