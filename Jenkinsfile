pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'shishir78/quothub-app:v1'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/shishir787/QuoteHub.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    sh 'docker push ${DOCKER_IMAGE}'
                }
            }
        }
    }
    post {
        always {
            cleanWs() // Clean up workspace after the build
        }
    }
}

