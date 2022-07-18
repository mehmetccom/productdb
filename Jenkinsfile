pipeline {
    agent any
    stages {
    
        stage('Undeploy') {
            steps {                                      
                echo 'Undeploy the web app..'                
                echo 'docker rm -vf $(docker ps -aq)'
                sh 'docker ps -aq | xargs docker rm -vf'
                
                echo 'docker rmi -f $(docker images -aq)'
                sh 'docker images -aq | xargs docker rmi -f'
            }
        }
    
        stage('Build') {
            steps {                                      
                echo 'Build the web app..'
                               
                dir('/home/mehmet/prj') {
                
                    sh 'rm -rf ./productdb'
                    sh 'git clone https://github.com/mehmetccom/productdb'
                    sh 'cd /home/mehmet/prj/productdb'
                    sh 'pwd'
                    sh 'ls -lR'
                    sh 'docker image build -t product-app-demo-image-1 .'
                }                                
            }
        }
                
        stage('Deploy') {
            steps {
                script{
                    echo 'Deploy the web app..'                    
                    sh 'docker run -p 5000:5000 -d --name product-app-demo-container-1 product-app-demo-image-1'
                }
            }
        }
        
        
    }
}
