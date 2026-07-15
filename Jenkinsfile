pipeline {
    agent any

    tools {
        // CRITICAL: This MUST match the exact name from your screenshot!
        sonarRunner 'sonar-scanner'
    }

    stages {
        stage('Step 1: Fetch Code') {
            steps {
                // Pulls your project files into Jenkins workspace
                checkout scm
            }
        }

        stage('Step 2: Scan Code Quality') {
            steps {
                // Connects Jenkins to the SonarQube server configuration
                withSonarQubeEnv('MY-SONAR-SERVER') {
                    
                    // Because your scanner is on Windows, we use 'bat' instead of 'sh'
                    bat '''
                        sonar-scanner \
                        -Dsonar.projectKey=my-local-windows-project \
                        -Dsonar.projectName="My Local Windows Project" \
                        -Dsonar.sources=. 
                    '''
                    
                }
            }
        }
    }
}