package {'jfryman-nginx':
    ensure => 'installed',
}
include nginx

class{'nginx':
    manage_repo => true,
    package_source => 'nginx-mainline'
}
nginx::resource::vhost {'default':
    location_cfg_append => {
        'rewrite' => '^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;'
    }
}
file { '/var/www/html/index.html':
    content => 'Hello World!'
}
file { '/var/www/html/error404.html':
    content => "Ceci n'est pas une page"
}
