pipeline {
    agent any
    stages {
    
        stage('Undeploy') {
            steps {                                      
                echo 'Undeploy the web app..'                
                echo 'sudo docker rm -vf $(sudo docker ps -aq)'
                sh 'sudo docker ps -aq | xargs sudo docker rm -vf'
                
                echo 'sudo docker rmi -f $(sudo docker images -aq)'
                sh 'sudo docker images -aq | xargs sudo docker rmi -f'
            }
        }
    
        stage('Build') {
            steps {                                      
                echo 'Build the web app..'
                               
                dir('/home/mehmet/prj') {                             
                    sh 'sudo git clone https://github.com/mehmetccom/productdb'
                    sh 'sudo cd /home/mehmet/prj/productdb'
                    sh 'sudo pwd'
                    sh 'sudo ls -lR'
                    sh 'sudo docker image build -t product-app-demo-image-1 .'
                }                                
            }
        }
                
        stage('Deploy') {
            steps {
                script{
                    echo 'Deploy the web app..'                    
                    sh 'sudo docker run -p 5000:5000 -d --name product-app-demo-container-1 product-app-demo-image-1'
                }
            }
        }
        
        
    }
}
