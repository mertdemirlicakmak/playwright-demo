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
                junit 'results.xml'
            }
        }
    }

    post {
        // always {
        //     junit 'results.xml'
        // }
        failure {
            echo 'Tests failed!'
            archiveArtifacts artifacts: 'screenshots/*.png', fingerprint: true
        }
    }
}