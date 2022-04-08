pipeline {
    agent any
    stages {
        stage('Run unit tests') {
            steps {
                sh "bash test.sh"
            }
        }
        stage('Build and push images') {
            environment {
                DOCKER_CREDS = credentials('docker-creds')
            }
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u ${DOCKER_CREDS_USR} -p ${DOCKER_CREDS_PSW}"
                sh "docker-compose push"
            }
        }
        stage('Deploy') {
            steps {
                sh "echo '    driver: overlay' >> docker-compose.yml" 
                sh "scp ./docker-compose.yml jenkins@swarm-manager:/home/jenkins/docker-compose.yml"
                sh "scp ./nginx.conf jenkins@swarm-manager:/home/jenkins/nginx.conf"
                sh "ssh jenkins@swarm-manager < deploy.sh"
                // sh "ssh jenkins@swarm-manager 'docker stack deploy --compose-file docker-compose.yml prac-proj-stack'"
                
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: "*/htmlcov/*"
        }
    }
}