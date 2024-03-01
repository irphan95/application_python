pipeline {
    agent any
    
    environment {
        registry = "irphan964/python_apps"
        dockerImage = ''
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master',
                credentialsId: 'git_hub',
                url: 'https://github.com/irphan95/application_python.git'
            }
        }

        stage ('Test') {
            steps {
                sh "pytest testRoutes.py"
            }
        }

        stage('Build Image') {
            steps {
                script {
                    def imageTag = "${env.BUILD_ID}"
                    dockerImage = docker.build("${registry}:${imageTag}")
                }
            }
        }

        stage('Push To DockerHub') {
            steps {
                script {
                    docker.withRegistry('', 'docker_hub') {
                        dockerImage.push()
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    def deployedContainer = docker.run("-d -p 5000:5000 --name ${JOB_NAME} ${registry}:${env.BUILD_ID}")
                    // Check for deployment success and perform necessary actions
                    if (deployedContainer) {
                        echo "Application deployed successfully."
                    } else {
                        error "Failed to deploy application."
                    }
                }
            }
        }
    }

    post {
        always {
            // Cleanup steps
            sh 'docker stop ${JOB_NAME} || true'
            sh 'docker rm ${JOB_NAME} || true'
            sh 'docker rmi ${registry}:${env.BUILD_ID} || true'
        }
    }
}
