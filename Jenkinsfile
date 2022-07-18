pipeline {
    agent any
    stages {
    
        stage('Get From Version Control') {
            steps {                                      
                echo 'Get the webapp from version control..'
                               
                dir('/home/mehmet/prj/productdb') {
                    deleteDir()
                }    
                
                dir('/home/mehmet/prj') {                    
                    sh 'git clone https://github.com/mehmetccom/productdb'
                }                
            }
        }
    
        stage('Test') {
            steps {                                      
                echo 'Test the web app..'
                sh 'python /home/mehmet/prj/productdb/test.py'                               
            }
        }
        
        stage('Undeploy') {
            steps {                                      
                echo 'Undeploy the web app..'                
                echo 'sudo docker rm -vf $(sudo docker ps -aq)'
                sh 'sudo docker ps -aq | xargs sudo docker rm -vf'
                
                echo 'sudo docker rmi -f $(sudo docker images -aq)'
                sh 'sudo docker images -aq | xargs sudo docker rmi -f'
            }
        }
        
        stage('Docker Image Build') {
            steps {                                      
                echo 'Build the web app..'
                               
                dir('/home/mehmet/prj/productdb') {                    
                    sh 'pwd'
                    sh 'ls -lR'
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

