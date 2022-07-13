pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Build') {
          steps {
            echo 'Please place your build command or script here'
          }
        }
      }
    }

    stage('Test') {
      steps {
        echo 'All test functions is in test.py file. Lets run tests...'
        sh 'python3 test.py'
      }
    }

    stage('Deploy')
    {
      steps {
        echo 'Deploying the Flask web application..'
        echo 'Please place your own deployment command or script in here'
      }
    }

  }

  post {
        always {
            echo 'The pipeline completed'
        }
        success {            
            sh 'sudo nohup python3 app.py > log.txt 2>&1 &'
            echo 'Flask web application up and running!'
        }
        failure {
            echo 'Build stage failed'
            error('Stopping the application..')
        }
      }
}