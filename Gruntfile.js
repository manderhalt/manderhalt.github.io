module.exports = function(grunt) {

    grunt.initConfig({
        express: {
            all: {
                options: {
                    bases: ['.'],
                    port: 8080,
                    hostname: "127.0.0.1",
                    livereload: true
                }
            }
        },
        watch: {
            all: {
                files: '**/*.html',
                options: {
                    livereload: true
                }
            },
            less:{
                files:'less/*.less',
                tasks:['less']
            },
            js:{
                files:'js/mapheader.js',
                options: {
                    livereload: true
                }
            }
        },
        less: {
            development : {
                options:{},
                files: {
                    "css/agency.css": "less/agency.less"
                }
            }
        }


    });

    grunt.event.on('watch', function(action, filepath, target) {
        grunt.log.writeln(target + ': ' + filepath + ' has ' + action);
    });

    grunt.loadNpmTasks('grunt-express');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.registerTask('default', ['express','watch','less']);

};
