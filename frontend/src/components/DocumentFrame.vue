<template>
  <div class="document-frame">
    <div
      style="
        padding-left: 1%;
        padding-right: 1%;
        width: 100%;
        height: 100%;
        position: relative;
        box-sizing: border-box;
      "
    >
      <div class="document-content-frame">
        <div class="cover-frame">
          <img v-bind:src="cover" class="cover" />
        </div>
        <div class="detail-frame">
          <p class="title detail">{{ title }}</p>
          <p class="fingerprint detail">Fingerprint(SHA256): {{ fingerprint }}</p>
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
  max-width: 33%;
  width: 95%;
  margin-left: 2.5%;
  margin-right: 2.5%;
  margin-top: 20px;
  max-height: 500px;
  max-width: 400px;
}

.document-content-frame {
  height: 100%;
  width: 100%;
  border-radius: 25px;
  display: flex;
  background: #D3DBDA;
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
  border: 1px solid black;
  border-bottom: none;
  border-top-left-radius: 25px;
  border-top-right-radius: 25px;
}

.cover:hover {
    -webkit-transform: scale(1.2);
    -moz-transform: scale(1.2);
    -o-transform: scale(1.2);
    -ms-transform: scale(1.2);
    transform: scale(1.2);
    border-radius: 20px;
    border: 1px solid black;
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
  font-weight: bold;
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

@media screen and (min-width: 1200px) {
  .document-frame {
    width: 20%;
  }
}
</style>
