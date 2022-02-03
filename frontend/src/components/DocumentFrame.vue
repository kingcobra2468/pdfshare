<template>
  <div class="document-frame">
    <div>
      <div class="document-content-frame">
        <div class="cover-frame">
          <img v-bind:src="'http://0.0.0.0:9000/static/covers/' + title + '.png'" class="cover" />
        </div>
        <div class="detail-frame">
          <p class="title detail">{{ title }}</p>
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
}

.fingerprint {
  color: black;
  font-size: 0.8em;
  overflow-wrap: break-word;
  height: 40%;
  word-break: break-all;
}

.fingerprint > span {
  font-weight: 500;
}

@media screen and (min-width: 1200px) {
  .document-frame {
    width: 20%;
  }
}
</style>
