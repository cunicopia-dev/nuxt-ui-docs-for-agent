<!-- source: https://ui.nuxt.com/components/page-logos --> # PageLogosPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/PageLogos.vue)

A list of logos or images to display on your pages.

## Usage

The PageLogos component provides a flexible way to display a list of logos or
images in your pages.

### Title

Use the `title` prop to set the title above the logos.

title

## Trusted by the best front-end teams

    
    
    <template>
      <UPageLogos
        title="Trusted by the best front-end teams"
        :items="[
          'i-simple-icons-github',
          'i-simple-icons-discord',
          'i-simple-icons-x',
          'i-simple-icons-instagram',
          'i-simple-icons-linkedin',
          'i-simple-icons-facebook'
        ]"
      />
    </template>
    

### Items

You can display logos in two ways:

  1. Using the `items` prop to provide a list of logos. Each item can be either:

  * An icon name (e.g., `i-simple-icons-github`)
  * An object containing `src` and `alt` properties for images, which will be utilized in a `UAvatar` component

  2. Using the default slot to have complete control over the content

With ItemsWith Slot

## Trusted by the best front-end teams

    
    
    <script setup lang="ts">
    const items = [
      'i-simple-icons-github',
      'i-simple-icons-discord',
      'i-simple-icons-x',
      'i-simple-icons-instagram',
      'i-simple-icons-linkedin',
      'i-simple-icons-facebook'
    ]
    </script>
    
    <template>
      <UPageLogos title="Trusted by the best front-end teams" :items="items" />
    </template>
    

## Trusted by the best front-end teams

    
    
    <template>
      <UPageLogos title="Trusted by the best front-end teams">
        <UIcon name="i-simple-icons-github" class="size-10 shrink-0" />
        <UIcon name="i-simple-icons-discord" class="size-10 shrink-0" />
        <UIcon name="i-simple-icons-x" class="size-10 shrink-0" />
        <UIcon name="i-simple-icons-instagram" class="size-10 shrink-0" />
        <UIcon name="i-simple-icons-linkedin" class="size-10 shrink-0" />
        <UIcon name="i-simple-icons-facebook" class="size-10 shrink-0" />
      </UPageLogos>
    </template>
    

### Marquee

Use the `marquee` prop to enable a marquee effect for the logos.

title

## Trusted by the best front-end teams

    
    
    <template>
      <UPageLogos
        title="Trusted by the best front-end teams"
        marquee
        :items="[
          'i-simple-icons-github',
          'i-simple-icons-discord',
          'i-simple-icons-x',
          'i-simple-icons-instagram',
          'i-simple-icons-linkedin',
          'i-simple-icons-facebook'
        ]"
      />
    </template>
    

[](/components/page-marquee)When you use `marquee` mode, you can customize its
behavior by passing props. For more info, check out the
[PageMarquee](/components/page-marquee) component.

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`marquee`| `false`| `boolean | PageMarqueeProps`Show properties

  * `as?: any`The element or component this component should render as. Defaults to `'div'`.
  * `pauseOnHover?: boolean`
  * `reverse?: boolean`
  * `orientation?: "horizontal" | "vertical"`
  * `repeat?: number`
  * `overlay?: boolean`
  * `class?: any`
  * `ui?: { root?: ClassNameValue; content?: ClassNameValue; }`

  
`items`| | ` PageLogosItem[]`Show properties

  * `src: string`
  * `alt: string`

  
`title`| | ` string`  
`ui`| | ` { root?: ClassNameValue; title?: ClassNameValue; logos?: ClassNameValue; logo?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`default`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        pageLogos: {
          slots: {
            root: 'relative overflow-hidden',
            title: 'text-lg text-center font-semibold text-highlighted',
            logos: 'mt-10',
            logo: 'size-10 shrink-0'
          },
          variants: {
            marquee: {
              false: {
                logos: 'flex items-center shrink-0 justify-around gap-(--gap) [--gap:--spacing(16)]'
              }
            }
          }
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          uiPro: {
            pageLogos: {
              slots: {
                root: 'relative overflow-hidden',
                title: 'text-lg text-center font-semibold text-highlighted',
                logos: 'mt-10',
                logo: 'size-10 shrink-0'
              },
              variants: {
                marquee: {
                  false: {
                    logos: 'flex items-center shrink-0 justify-around gap-(--gap) [--gap:--spacing(16)]'
                  }
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          uiPro: {
            pageLogos: {
              slots: {
                root: 'relative overflow-hidden',
                title: 'text-lg text-center font-semibold text-highlighted',
                logos: 'mt-10',
                logo: 'size-10 shrink-0'
              },
              variants: {
                marquee: {
                  false: {
                    logos: 'flex items-center shrink-0 justify-around gap-(--gap) [--gap:--spacing(16)]'
                  }
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

[PageListA vertical list layout for displaying content in a stacked
format.](/components/page-list)[PageMarqueeA component to create infinite
scrolling content.](/components/page-marquee)

