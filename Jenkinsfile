pipeline {
    agent any

    environment {
        VENV_DIR = ".venv"
    }

    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }
        stage('Build docker image') {
            steps {
                sh './test.sh build-image'
            }
        }
        stage('Run Linters') {
            steps {
                sh './test.sh run-linters'
            }
        }
        stage('Run Tests In Docker') {
            steps {
                sh './test.sh test-docker -m basic_search'
            }
        }
    }

    post {
        always {
            junit 'results.xml'
        }
    }
}