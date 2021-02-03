% include('header.tpl')

<section class="section">
  <div class="columns is-centered is-widescreen">
    <div class="column is-half">
    <div class="notification card is-light">
    <div class="container px-4">


        <p class="title mb-0">Vocab</p>
        <p>
          Words for hang-man, word-searches, bingo, charades or pictionary!
        </p>

        <form action="." class="mt-4">


          <div class="field is-horizontal">
            <div class="field-body">

              <div class="field">
                <p class="label">Level</p>
                <span class="select">
                  <select id="level" name="level" value={{level}}>
                    %for lvl in levels:
                      <option value="{{lvl}}" {{!'selected="selected"' if level == lvl else ""}}>{{lvl}}</option>
                    %end
                  </select>
                </span>
              </div>

              <div class="field">
                <p class="label">Quantity</p>
                <input style="width: 100px;" type="number" class="input mb-4" id="quantity" name="quantity" min="1" value="{{quantity}}" step="1">
              </div>

            </div>
          </div>

          <input type="submit" value="Get words" class="button is-link is-large is-fullwidth">

          %if words:
            % include('list.tpl')
          %end

        </form>

        <p class="help mt-4">

          This app is designed for APAX April teachers. It will give a random
          sample of words taken from all of the lessons in a given level. The
          words are random each time, refreshing the page will give a different
          list of words. Students should have seen all of these words by the
          end of B3. Select which level you want words from, then you can
          change how many words you want, even hundreds!

        </p>
      </div>
      </div>
      </div>
    </div>
</section>

% include('footer.tpl')
