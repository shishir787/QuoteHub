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
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh '''
                        echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                        docker push $DOCKER_IMAGE
                    '''
                }
            }
        }

        stage('Deploy Updated Container') {
            steps {
                sh '''
                    docker stop quothub || true
                    docker rm quothub || true
                    docker pull $DOCKER_IMAGE
                    docker run -d -p 5000:5000 --name quothub $DOCKER_IMAGE
                '''
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
