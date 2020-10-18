import React from "react";
import demo from "../../static/frontend/img/top/demo.png"
import quest from "../../static/frontend/img/top/quest.png"


class Top extends React.Component {
  render() {
    return (
      <div class="back bgmask">
        <div class="container">
          <div class="front">
            <div className="catchblock">
              <div className="catch brownfont">
                <h1>今日のおつまみ、<br />何にしよう。</h1>
                <br />
                <p className="title_sentence brownfont">
                  今日飲む予定のお酒に合わせて、<br />
          AIがおつまみを提案。<br />
                  <br />
          写真を撮って質問に答えるだけで、<br />
          あなたの今日のおつまみが決まります！<br />
                  <br />
                  <ul className="top_menu">
                    <li><a href="#howto" className="brownbtn whitefont">使い方</a></li>
                    <li><a href="submit" className="brownbtn whitefont">おつまみを決める</a></li>
                  </ul>
                </p>

              </div>
            </div>
          </div>
        </div>
        <div className="howtouse">
          <div id="howto" >
            <h1>HOW TO USE</h1>
            <h2>使い方</h2>
            <ul className="demo">
              <li>①お酒の写真を撮って…… <br />
                <img src={demo} /></li><br />
              <li>②n問の質問に答えるだけ！<br />
                <img src={quest} /></li><br />
            </ul>
            <br />
          </div>
        </div>
      </div>
    );
  }
}
export default Top;

