from crypt import methods
from flask import render_template, Blueprint, request, redirect, url_for, flash
from personalweb.project.models import Project
from personalweb import db

project = Blueprint('project', __name__)

@project.route('/projects')
@project.route('/projects/index')
def show_projects():
  projects = Project.query.all()
  db.session.commit()
  return render_template('project/index.html', projects = projects)

@project.route('/projects/create')
def create():
  return render_template('/project/create.html')

@project.route('/projects/insert', methods=['POST'])
def insert():
  # retrieve form data
  title = request.form.get('title')
  description = request.form.get('description')
  
  # save data in a objetc
  project = Project(title, description)
  
  # send data to db
  db.session.add(project)
  db.session.commit()
  
  flash('Project added')
  
  # redirect home page
  return redirect(url_for('project.show_projects'))

@project.route('/projects/edit/<int:id>')
def edit(id):
  project = Project.query.get_or_404(id)
  return render_template('project/edit.html', project = project)

@project.route('/projects/update/<int:id>', methods=['POST'])
def update(id):
  project = Project.query.get_or_404(id)
  project.title = request.form.get('title')
  project.description = request.form.get('description')
  
  db.session.add(project)
  db.session.commit()
  flash('Project edited')
  return redirect(url_for('project.show_projects'))

@project.route('/projects/delete/<int:id>')
def delete(id):
  project = Project.query.get_or_404(id)
  
  db.session.delete(project)
  db.session.commit()
  flash('Project deleted')
  return redirect(url_for('project.show_projects'))