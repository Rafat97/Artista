const mix = require('laravel-mix');
// mix.browserSync('http://127.0.0.1:8000/js/framework/');

mix.react('static/js/framework/react_js/index.js', 'static/js/public/app-react.js')
    //.extract()
    /**
     * 
     * NOTE !! No need to use lazy-loading this project
     * 
     * How to lazy-loading components in react 
     * https://reactjs.org/docs/code-splitting.html
     * 
     * example : const OtherComponent = React.lazy(() => import('./OtherComponent'));
     */
    .webpackConfig({
        output: { chunkFilename: 'static/js/public/chunks-react/react-[name].js?id=[chunkhash]' },
    });

mix.js('static/js/framework/vue_js/main.js', 'static/js/public/app-vue.js')
    //.extract()
    /**
     * 
     * NOTE !! No need to use lazy-loading this project
     * 
     *  
     * How to lazy-loading components in vue 
     * https://router.vuejs.org/guide/advanced/lazy-loading.html
     * 
     * example : const Foo = () => import('./Foo.vue')
     */
    .webpackConfig({
        output: { chunkFilename: 'static/js/public/chunks-vue/vue-[name].js?id=[chunkhash]' },
    });

        
