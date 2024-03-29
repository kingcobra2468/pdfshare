<template>
  <div class="document-frame">
    <div>
      <div class="document-content-frame">
        <div class="cover-frame">
          <a
            class="cover cover-frame"
            v-bind:href="this.$data.baseUrl + '/static/books/' + title + '.pdf'"
          >
            <img
              v-bind:src="$data.baseUrl + '/static/covers/' + title + '.jpeg'"
              class="cover"
              @error="setDefaultCover"
            />
          </a>
        </div>
        <div class="detail-frame">
          <div>
            <p class="title detail">{{ title }}</p>
            <a
              class="icon-frame detail"
              v-bind:href="$data.baseUrl + '/v1/download?pdfTitle=' + title"
            >
              <img class="download-icon" src="@/assets/icons/download.svg" />
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
  props: {
    title: String,
    cover: String,
    fingerprint: String,
  },
  data() {
    return {
      baseUrl: process.env.VUE_APP_BASE_URL ?? '',
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
};
</script>

<style scoped>
.document-frame {
  display: block;
  min-width: 300px;
  width: 95%;
  padding-left: 2.5%;
  padding-right: 2.5%;
  margin-top: 50px;
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
  align-items: center;
}

.cover {
  height: 100%;
  border-radius: 10px;
  box-shadow: var(--document-frame-shadow);
}

.detail {
  display: block;
  font-family: "Mukta";
  color: var(--text-primary-color);
  margin: 0;
  padding-top: 3%;
  text-align: left;
  padding-left: 2.5%;
  padding-right: 2.5%;
}

.title {
  font-weight: 600;
  color: var(--text-primary-color);
  font-size: 1.2em;
  text-overflow: ellipsis;
  overflow: hidden;
  max-height: 60%;
  white-space: nowrap;
  width: 90%;
}

.fingerprint {
  color: var(--text-primary-color);
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
  max-height: 20px;
  align-content: flex-end;
  filter: var(--icon-primary-color);
}

@media screen and (min-width: 1200px) {
  .document-frame {
    width: 20%;
  }
}
</style>
