pipeline {
    agent any
    stages {
        stage('test') {
            steps {
                sh "bash test.sh"
            }
        }

        }
    }
    post {
        always {
            junit '**/*.xml'
            cobertura coberturaReportFile: 'service-1/coverage.xml', failNoReports: false

        }
    }