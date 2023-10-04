from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message


app = Flask(__name__)