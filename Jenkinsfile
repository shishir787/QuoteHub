pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "shishir78/quotehub:latest"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/shishir787/quotehub.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {
                    sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push $DOCKER_IMAGE'
            }
        }

        stage('Deploy Updated Container') {
            steps {
                sh '''
                    docker stop quotehub || true
                    docker rm quotehub || true
                    docker pull $DOCKER_IMAGE
                    docker run -d -p 5000:5000 --name quotehub $DOCKER_IMAGE
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

