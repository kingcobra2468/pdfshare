<template>
  <div class="document-frame">
    <div>
      <div class="document-content-frame">
        <div class="cover-frame">
          <a class="cover cover-frame" v-bind:href="this.$data.baseUrl
           + '/static/books/' + title + '.pdf'">
            <img v-bind:src="$data.baseUrl + '/static/covers/'
            + title + '.png'" class="cover"
            @error="setDefaultCover"/>
          </a>
        </div>
        <div class="detail-frame">
          <div>
            <p class="title detail">{{ title }}</p>
            <a class="icon-frame detail" v-bind:href="$data.baseUrl
            + '/v1/download?pdfTitle=' + title">
              <img class="download-icon" src='@/assets/icons/download.png'>
            </a>
          </div>
          <p class="fingerprint detail">
            <span>Fingerprint(SHA256):</span> {{ fingerprint }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DocumentFrame',
  data() {
    return {
      baseUrl: process.env.VUE_APP_BASE_URL,
    };
  },
  computed: {
    /* eslint-disable global-require */
    defaultCover() {
      return require('@/assets/images/default_cover.jpg');
    },
  },
  methods: {
    /* eslint no-param-reassign: "error" */
    setDefaultCover(event) {
      event.target.src = this.defaultCover;
    },
  },
  props: {
    title: String,
    cover: String,
    fingerprint: String,
  },
};
</script>

<style scoped>
.document-frame {
  display: block;
  min-width: 300px;
  width: 95%;
  padding-left: 2.5%;
  padding-right: 2.5%;
  margin-top: 20px;
  max-height: 500px;
  max-width: 400px;
}

.document-frame > div {
  padding-left: 1%;
  padding-right: 1%;
  width: 100%;
  height: 100%;
  position: relative;
  box-sizing: border-box;
}
.document-content-frame {
  height: 100%;
  width: 100%;
  border-radius: 25px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.cover-frame {
  display: flex;
  flex-direction: column;
  align-content: center;
  justify-content: center;
  height: 80%;
  width: 100%;
}

.detail-frame {
  display: flex;
  flex-direction: column;
  width: 100%;
  align-content: center;
}

.detail-frame > div {
  height: 100%;
  display: flex;
  align-items: flex-end;
}

.cover {
  height: 100%;
  border-radius: 10px;
  box-shadow: 0 3px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}

.detail {
  display: block;
  font-family: "Mukta";
  color: black;
  margin: 0;
  padding-top: 3%;
  text-align: left;
  padding-left: 2.5%;
  padding-right: 2.5%;
}

.title {
  font-weight: 600;
  color: black;
  font-size: 1.2em;
  text-overflow: ellipsis;
  overflow: hidden;
  max-height: 60%;
  white-space: nowrap;
  width: 90%;
}

.fingerprint {
  color: black;
  font-size: 0.8em;
  overflow-wrap: break-word;
  height: 40%;
  word-break: break-all;
}

.fingerprint > span {
  font-weight: bold;
}

.icon-frame {
  display: flex;
  flex-direction: row-reverse;
  width: 10%;
}

.download-icon {
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 20px;
  align-content: flex-end;
}

@media screen and (min-width: 1200px) {
  .document-frame {
    width: 20%;
  }
}
</style>
