Rails.application.routes.draw do

  resources :articles
  
  	#get "/articles"
  	#post "/articles"
  	#delete "/articles"
  	#get "/articles/:id"
  	#get "/articles/: new"
  	#get "/articles/:id/edit"
  	#patch "/articles/:id"
  	#put "/articles/:id"
  get 'lista/index'

  get 'welcome/index'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
