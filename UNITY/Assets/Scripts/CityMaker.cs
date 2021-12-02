using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CityMaker : MonoBehaviour
{
    [SerializeField] TextAsset layout;
    [SerializeField] GameObject roadPrefab;
    [SerializeField] GameObject buildingPrefab;
    [SerializeField] GameObject semaphorePrefab;
    [SerializeField] GameObject junctionPrefab;
    [SerializeField] GameObject junctionPrefabBorder;
    [SerializeField] GameObject junctionPrefabNormal;
    [SerializeField] GameObject passPrefab;
    [SerializeField] GameObject cornerPrefab;
    [SerializeField] GameObject cornerInsidePrefab;
    
    [SerializeField] int tileSize;
    
    public List<GameObject> trafficLights;
    public static CityMaker Instance;

    // Start is called before the first frame update
    void Start()
    {
    	Instance = this;
        MakeTiles(layout.text);
        defaultTrafficLightsConfig();
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    
    void defaultTrafficLightsConfig() {
    	trafficLights[0].transform.GetChild(2).gameObject.SetActive(true);
    	trafficLights[1].transform.GetChild(2).gameObject.SetActive(true);
    	trafficLights[2].transform.GetChild(0).gameObject.SetActive(true);
    	trafficLights[3].transform.GetChild(0).gameObject.SetActive(true);
    	trafficLights[4].transform.GetChild(2).gameObject.SetActive(true);
    	trafficLights[5].transform.GetChild(2).gameObject.SetActive(true);
    	trafficLights[6].transform.GetChild(2).gameObject.SetActive(true);
    	trafficLights[7].transform.GetChild(2).gameObject.SetActive(true);
    	trafficLights[8].transform.GetChild(0).gameObject.SetActive(true);
    	trafficLights[9].transform.GetChild(0).gameObject.SetActive(true);
    	trafficLights[10].transform.GetChild(0).gameObject.SetActive(true);
    	trafficLights[11].transform.GetChild(0).gameObject.SetActive(true);
    	trafficLights[12].transform.GetChild(0).gameObject.SetActive(true);
    	trafficLights[13].transform.GetChild(0).gameObject.SetActive(true);
    	trafficLights[14].transform.GetChild(0).gameObject.SetActive(true);
    	trafficLights[15].transform.GetChild(0).gameObject.SetActive(true);
    	trafficLights[16].transform.GetChild(2).gameObject.SetActive(true);
    	trafficLights[17].transform.GetChild(2).gameObject.SetActive(true);
    	trafficLights[18].transform.GetChild(2).gameObject.SetActive(true);
    	trafficLights[19].transform.GetChild(2).gameObject.SetActive(true);
    	trafficLights[20].transform.GetChild(2).gameObject.SetActive(true);
    	trafficLights[21].transform.GetChild(2).gameObject.SetActive(true);
    	trafficLights[22].transform.GetChild(0).gameObject.SetActive(true);
    	trafficLights[23].transform.GetChild(0).gameObject.SetActive(true);
    	trafficLights[24].transform.GetChild(0).gameObject.SetActive(true);
    	trafficLights[25].transform.GetChild(0).gameObject.SetActive(true);
    	trafficLights[26].transform.GetChild(2).gameObject.SetActive(true);
    	trafficLights[27].transform.GetChild(2).gameObject.SetActive(true);
    }

    void MakeTiles(string tiles)
    {
        int x = 0;
        int y = 0;

        Vector3 position;
        Vector3 positionSema;
        GameObject tile;

        for (int i=0; i<tiles.Length; i++) {
            if (tiles[i] == '>') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(roadPrefab, position, Quaternion.Euler(0, 90, 0));
                tile.transform.parent = transform;
                x += 1;
            } else if (tiles[i] == '<') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(roadPrefab, position, Quaternion.Euler(0, 270, 0));
                tile.transform.parent = transform;
                x += 1;
            }else if (tiles[i] == 'v') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(roadPrefab, position, Quaternion.Euler(0, 0, 0));  //(0, 90, 0)
                tile.transform.parent = transform;
                x += 1;
            } else if (tiles[i] == '^') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(roadPrefab, position, Quaternion.Euler(0, 180, 0));  //(0, 90, 0)
                tile.transform.parent = transform;
                x += 1;
            }else if (tiles[i] == '8') { //check
                positionSema = new Vector3((x * tileSize)+0.45f, 0, y * tileSize);
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(passPrefab, position, Quaternion.Euler(0, 180, 0));
                tile.transform.parent = transform;
                tile = Instantiate(semaphorePrefab, positionSema, Quaternion.Euler(0, 180, 0));
                tile.transform.parent = transform;
                trafficLights.Add(tile);
                x += 1;
            }else if (tiles[i] == 's') { //check
                positionSema = new Vector3((x * tileSize)-0.45f, 0, y * tileSize);
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(passPrefab, position, Quaternion.Euler(0, 180, 0));
                tile.transform.parent = transform;
                tile = Instantiate(semaphorePrefab, positionSema, Quaternion.Euler(0, 180, 0));
                tile.transform.parent = transform;
                trafficLights.Add(tile);
                x += 1;
            } else if (tiles[i] == 'g') { //check
                positionSema = new Vector3(x * tileSize, 0, (y * tileSize)-0.45f);
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(passPrefab, position, Quaternion.Euler(0, 270, 0));
                tile.transform.parent = transform;
                tile = Instantiate(semaphorePrefab, positionSema, Quaternion.Euler(0, 270, 0));
                tile.transform.parent = transform;
                trafficLights.Add(tile);
                x += 1;
            } else if (tiles[i] == '6') { //check
                positionSema = new Vector3(x * tileSize, 0, (y * tileSize)+0.45f);
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(passPrefab, position, Quaternion.Euler(0, 270, 0));
                tile.transform.parent = transform;
                tile = Instantiate(semaphorePrefab, positionSema, Quaternion.Euler(0, 270, 0));
                tile.transform.parent = transform;
                trafficLights.Add(tile);
                x += 1;
            }else if (tiles[i] == '2') { //check
                positionSema = new Vector3((x * tileSize)+0.45f, 0, y * tileSize);
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(passPrefab, position, Quaternion.Euler(0, 0, 0));
                tile.transform.parent = transform;
                tile = Instantiate(semaphorePrefab, positionSema, Quaternion.Euler(0, 0, 0));
                tile.transform.parent = transform;
                trafficLights.Add(tile);
                x += 1;
            }else if (tiles[i] == 'z') { //check
                positionSema = new Vector3((x * tileSize)-0.45f, 0, y * tileSize);
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(passPrefab, position, Quaternion.Euler(0, 0, 0));
                tile.transform.parent = transform;
                tile = Instantiate(semaphorePrefab, positionSema, Quaternion.Euler(0, 0, 0));
                tile.transform.parent = transform;
                trafficLights.Add(tile);
                x += 1;
            }else if (tiles[i] == 'A') { //check
            	positionSema = new Vector3(x * tileSize, 0, (y * tileSize)-0.45f);
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(passPrefab, position, Quaternion.Euler(0, 90, 0));  //(0, 90, 0)
                tile.transform.parent = transform;
                tile = Instantiate(semaphorePrefab, positionSema, Quaternion.Euler(0, 90, 0));
                tile.transform.parent = transform;
                trafficLights.Add(tile);
                x += 1;
            } else if (tiles[i] == '4') { //check
            	positionSema = new Vector3(x * tileSize, 0, (y * tileSize)+0.45f);
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(passPrefab, position, Quaternion.Euler(0, 90, 0));  //(0, 90, 0)
                tile.transform.parent = transform;
                tile = Instantiate(semaphorePrefab, positionSema, Quaternion.Euler(0, 90, 0));
                tile.transform.parent = transform;
                trafficLights.Add(tile);
                x += 1;
            }else if (tiles[i] == '7') { //check
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(junctionPrefabBorder, position, Quaternion.Euler(0, 90, 0));  //(0, 90, 0)
                tile.transform.parent = transform;
                x += 1;
            }else if (tiles[i] == '9') { //check
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(junctionPrefabBorder, position, Quaternion.Euler(0, 0, 0));  //(0, 90, 0)
                tile.transform.parent = transform;
                x += 1;
            }else if (tiles[i] == '1') { //check
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(junctionPrefabBorder, position, Quaternion.Euler(0, 180, 0));  //(0, 90, 0)
                tile.transform.parent = transform;
                x += 1;
            }else if (tiles[i] == '3') { //check
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(junctionPrefabBorder, position, Quaternion.Euler(0, 270, 0));  //(0, 90, 0)
                tile.transform.parent = transform;
                x += 1;
            }else if (tiles[i] == '/') { //check
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(junctionPrefabNormal, position, Quaternion.Euler(0, 270, 0));  //(0, 90, 0)
                tile.transform.parent = transform;
                x += 1;
            }else if (tiles[i] == '\\') { //check
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(junctionPrefabNormal, position, Quaternion.Euler(0, 0, 0));  //(0, 90, 0)
                tile.transform.parent = transform;
                x += 1;
            }else if (tiles[i] == '_') { //check
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(junctionPrefabNormal, position, Quaternion.Euler(0, 180, 0));  //(0, 90, 0)
                tile.transform.parent = transform;
                x += 1;
            }else if (tiles[i] == '-') { //check
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(junctionPrefabNormal, position, Quaternion.Euler(0, 90, 0));  //(0, 90, 0)
                tile.transform.parent = transform;
                x += 1;
            }else if (tiles[i] == '[') { //check
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(cornerPrefab, position, Quaternion.Euler(0, 270, 0));  //(0, 90, 0)
                tile.transform.parent = transform;
                x += 1;
            }else if (tiles[i] == ']') { //check
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(cornerPrefab, position, Quaternion.Euler(0, 0, 0));  //(0, 90, 0)
                tile.transform.parent = transform;
                x += 1;
            }else if (tiles[i] == '{') { //check
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(cornerPrefab, position, Quaternion.Euler(0, 180, 0));  //(0, 90, 0)
                tile.transform.parent = transform;
                x += 1;
            }else if (tiles[i] == '}') { //check
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(cornerPrefab, position, Quaternion.Euler(0, 90, 0));  //(0, 90, 0)
                tile.transform.parent = transform;
                x += 1;
            }else if (tiles[i] == '(') { //check
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(cornerInsidePrefab, position, Quaternion.Euler(0, 270, 0));  //(0, 90, 0)
                tile.transform.parent = transform;
                x += 1;
            }else if (tiles[i] == ')') { //check
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(cornerInsidePrefab, position, Quaternion.Euler(0, 0, 0));  //(0, 90, 0)
                tile.transform.parent = transform;
                x += 1;
            }else if (tiles[i] == '¿') { //check
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(cornerInsidePrefab, position, Quaternion.Euler(0, 180, 0));  //(0, 90, 0)
                tile.transform.parent = transform;
                x += 1;
            }else if (tiles[i] == '?') { //check
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(cornerInsidePrefab, position, Quaternion.Euler(0, 90, 0));  //(0, 90, 0)
                tile.transform.parent = transform;
                x += 1;
            }else if (tiles[i] == 'D') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(buildingPrefab, position, Quaternion.Euler(0, 90, 0));
                tile.GetComponent<Renderer>().materials[0].color = Color.red;
                tile.transform.parent = transform;
                x += 1;
            } else if (tiles[i] == '#') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(buildingPrefab, position, Quaternion.identity);
                tile.transform.localScale = new Vector3(1, Random.Range(0.5f, 2.0f), 1);
                tile.transform.parent = transform;
                x += 1;
            } else if (tiles[i] == '.') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(junctionPrefab, position, Quaternion.identity);
                tile.transform.parent = transform;
                x += 1;
            } else if (tiles[i] == '\n') {
                x = 0;
                y += 1;
            }
        }

    }
}
