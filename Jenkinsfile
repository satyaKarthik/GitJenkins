pipeline {
    agent any
    environment {
            PATH = "C:\\Users\\sb186125\\AppData\\Local\\Programs\\Python\\Python39\\python.exe;${env.PATH}"
        }
    stages {
        stage('Build') {
            steps {
                bat 'PATH testing.py'
            }
        }
        stage('Test'){
            steps {
                bat 'PATH test_testing.py'
            }
        }
    }
}
