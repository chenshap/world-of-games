pipeline {
         agent any
         stages {
                 stage('Checkout') {
                    steps {
                    git 'https://github.com/chenshap/<PROJECT_NAME>.git'
                 }
                 }
                 stage('Build') {
                 steps {
                    input('Do you want to proceed?')
                 }
                 }
                 stage('Run') {
                 steps {
                                     input('Do you want to proceed?')
                                  }

                           }
                 stage('Test') {
                     steps {
                                echo "App is Prod Ready"
                              }
                 stage('Finalize') {
                                 steps {
                                    input('Do you want to proceed?')
                                 }
                                 }

              }
}
}