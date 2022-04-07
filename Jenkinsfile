pipeline {
    agent any
    stages {
        stage('Run unit tests') {
            steps {
                sh "bash test.sh"
            }
        }

        stage('build and push') {
            environment {
                DOCKER_CREDS = credentials('docker-cred')
            }
            steps {

                sh "docker-compose build --parallel"
                sh "docker login -u ${DOCKER_CREDS_USR} -p ${DOCKER_CREDS_PSW}"
                sh "docker-compose push"
                sh "/bin/bash -c 'docker rmi \$(docker images -q)'"
                
            }
        }

    }
    post {
        always {
            archiveArtifacts artifacts: "*/htmlcov/*"
        }
    }
}