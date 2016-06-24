desc "Manage web site publication"

# Settings
dest = "/mnt/MyWeb/scan"  # Destination

task :serve do
  sh "jekyll serve"
end

task :clean do
  sh "rm -rf _site"
end

task :build do
  sh "jekyll build"
end

task :deploy => [:build] do
  sh "rsync -avzL _site/ #{dest}"
end
