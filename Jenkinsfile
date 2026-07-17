pipeline {
    agent any

    stages {
        stage('Step 1: Fetch Project Files') {
            steps {
                cleanWs()
                checkout scm
            }
        }

        stage('Step 2: Scan Code Quality') {
            steps {
                // 1. Fetch your existing sonar-token from Jenkins
                withCredentials([string(credentialsId: 'sonar-token', variable: 'SONAR_PASSWORD')]) {
                    
                    // 2. Connect Jenkins to your SonarQube server configuration
                    withSonarQubeEnv('My-Sonar-Server') {
                        
                        script {
                            // 3. Dynamically resolve your local windows scanner tool path
                            def scannerHome = tool 'sonar-scanner'
                            
                            // 4. Run the scanner on your login script
                            bat """
                                "${scannerHome}\\bin\\sonar-scanner" \
                                -Dsonar.projectKey=my-local-windows-project \
                                -Dsonar.projectName="My Local Windows Project" \
                                -Dsonar.sources=. \
                                -Dsonar.token=${SONAR_PASSWORD}
                            """
                        }
                    }
                }
            }
        }

        stage('Step 3: Build Docker Image') {
            steps {
                echo 'Packaging the Login Web Application into a Docker Image...'
                // Compiles the Dockerfile using the local Docker engine
                bat 'docker build -t my-login-app:latest .'
            }
        }

        stage('Step 4: Deploy Application Container') {
            steps {
                echo 'Launching our Web Portal live...'
                script {
                    // Safe guard: Stop and remove any older running web application containers
                    bat 'docker stop my-web-portal || exit 0'
                    bat 'docker rm my-web-portal || exit 0'
                    
                    // Maps port 8501 of the container to port 8501 on your Windows desktop
                    bat 'docker run -d -p 8501:8501 --name my-web-portal my-login-app:latest'
                }
            }
        }
    }
}