from flask import Flask, render_template

app=Flask(__name__)


@app.route('/plot/')
def plot():
    from pandas_datareader import data
    #import fix_yahoo_finance
    from bokeh.plotting import figure,show,output_file
    from bokeh.embed import components
    from datetime import datetime
    from bokeh.resources import CDN
    Start=datetime(2016,10,1)
    End=datetime(2016,10,5)
    #data.DataReader?
    df=data.DataReader(name="GOOG",data_source="google",start=Start,end=End)
    df.index[df.Close>df.Open]
    p=figure(width=1000,height=300,x_axis_type='datetime',title="My candlestick chart")
    hours_12=12*60*60*1000
    p.rect(df.index[df.Close>df.Open],(df.Open+df.Close)/2,
        hours_12,abs(df.Open-df.Close),fill_color="green",line_color="black")
    p.rect(df.index[df.Close<df.Open],(df.Open+df.Close)/2,
        hours_12,abs(df.Open-df.Close),fill_color="red",line_color="black")

    #output_file('CS.html')
    #show(p)
    script1,div1=components(p)
    cdn_js=CDN.js_files[0]
    cdn_css=CDN.css_files[0]
    return render_template('plot.html',script1=script1,div1=div1,cdn_js=cdn_js,cdn_css=cdn_css)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')
if __name__=='__main__':
    app.run(debug=True)
